#! /bin/bash

	
	read -p "Enter the number os Workers: " nrWorkers

	re='^[0-9]+$'
	if ! [[ $nrWorkers =~ $re ]] ; then
   		echo "Error: Not a number" >&2; exit 1
	fi

	if [ "$(docker network ls -q -f name=ESLE_Network)" ]; then
		docker network rm ESLE_Network
		echo "Network ESLE_Network removed"
	fi

	if [ "$(docker volume ls -q -f name=ESLE_Volume)" ]; then
		docker volume rm ESLE_Volume
		echo "Volume ESLE_Volume remove"
	fi

	docker network create --attachable --driver overlay --ip-range 10.0.2.0/24 --subnet 10.0.0.0/16 ESLE_Network
	echo "Network ESLE_Network created"
	docker volume create ESLE_Volume
	echo "Volume ESLE_Volume created"

	#docker swarm leave --force
	#docker swarm init --advertise-addr 172.16.75.163 > getSwarm.txt
	#joinSwarm=$(sed '5q;d' getSwarm.txt)
	#rm ./getSwarm.txt

	#docker service create --name Containernet --mount source=ESLE_Project,target=/data \
	#--mount source=/var/run/docker.sock,target=/var/run/docker.sock,type=bind --replicas $nrWorkers \
	#--network ESLE_Project containernet/containernet

	chmod +x ./InstallMaxiNet.sh
	chmod +x ./MakeInstall.sh

	# Correr o Controlador
	docker run -d -it --name Controler --ip 10.0.1.1 --mount source=ESLE_Volume,target=/containernet --rm --privileged --pid='host' -v /var/run/docker.sock:/var/run/docker.sock --network ESLE_Network containernet/containernet /bin/bash
	ContainerID="$(docker ps -aqf 'name=Controler')"
	docker cp ./MaxiNet.cfg "Controler":/containernet/../etc/"MaxiNet.cfg"
	docker cp ./InstallMaxiNet.sh "Controler":/containernet/"InstallMaxiNet.sh"
	docker cp ./MakeInstall.sh "Controler":/containernet/"MakeInstall.sh"	
	docker exec -it "$ContainerID" ./InstallMaxiNet.sh
	gnome-terminal -x bash -c "docker exec -it '$ContainerID' python /pox/pox.py forwarding.l2_learning"

	# Correr o FrontendServer
	docker run -d -it --name "FrontendServer" --network ESLE_Network --ip 10.0.1.2 --mount source=ESLE_Volume,target=/containernet --rm --privileged --pid='host' -v /var/run/docker.sock:/var/run/docker.sock containernet/containernet /bin/bash
	ContainerID="$(docker ps -aqf 'name=FrontendServer')"
	docker cp ./MaxiNet.cfg "FrontendServer":/containernet/../etc/"MaxiNet.cfg"
	docker exec -it "$ContainerID" ./MakeInstall.sh
	gnome-terminal -x bash -c "docker exec -it '$ContainerID' MaxiNetFrontendServer"

	for ((i=1; ((i<=$nrWorkers)); i++)); do

		docker run -d -it --name "Containernet-$i" --network ESLE_Network --mount source=ESLE_Volume,target=/containernet --rm --privileged --pid='host' -v /var/run/docker.sock:/var/run/docker.sock containernet/containernet /bin/bash
		ContainerID="$(docker ps -aqf 'name='Containernet-$i'')"
		docker cp ./MaxiNet.cfg "Containernet-$i":/containernet/../etc/"MaxiNet.cfg"
		docker exec -it "$ContainerID" ./MakeInstall.sh
		gnome-terminal -x bash -c "docker exec -it '$ContainerID' MaxiNetWorker"

	done

exit
