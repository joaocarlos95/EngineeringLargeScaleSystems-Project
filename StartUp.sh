#! /bin/bash

	
	read -p "Enter the number os Workers: " nrWorkers

	re='^[0-9]+$'
	if ! [[ $nrWorkers =~ $re ]] ; then
   		echo "Error: Not a number" >&2; exit 1
	fi

	if [ ! "$(docker network ls -q -f name=ESLE_Network)" ]; then
		docker network rm ESLE_Network
	fi

	docker volume create ESLE_Volume
	docker network create --attachable -d overlay --ip-range=10.0.1.0/24 --subnet=10.0.0.0/16 ESLE_Network
	
	#docker swarm leave --force
	#docker swarm init --advertise-addr 172.16.75.163 > getSwarm.txt
	#joinSwarm=$(sed '5q;d' getSwarm.txt)
	#rm ./getSwarm.txt

	#docker service create --name Containernet --mount source=ESLE_Project,target=/data \
	#--mount source=/var/run/docker.sock,target=/var/run/docker.sock,type=bind --replicas $nrWorkers \
	#--network ESLE_Project containernet/containernet

	chmod +x ~/Desktop/InstallMaxiNet.sh

	# Correr o Controlador
	docker run -d --name 'Controler' --network ESLE_Network -it --ip 10.0.1.1 --mount source=ESLE_Volume,target=/containernet --rm --privileged --pid='host' -v /var/run/docker.sock:/var/run/docker.sock containernet/containernet /bin/bash
	ContainerID="$(docker ps -aqf 'name=Controler')"
	docker cp ~/Desktop/MaxiNet.cfg "Controler":/containernet/../etc/"MaxiNet.cfg"
	docker cp ~/Desktop/InstallMaxiNet.sh "Controler":/containernet/"InstallMaxiNet.sh"
	gnome-terminal -x bash -c "docker exec -it '$ContainerID' ./InstallMaxiNet.sh && cd /pox/ && python2 pox.py forwarding.l2_learning"

	# Correr o FrontendServer
	docker run -d --name 'FrontendServer' --network ESLE_Network -it --ip 10.0.1.2 --mount source=ESLE_Volume,target=/containernet --rm --privileged --pid='host' -v /var/run/docker.sock:/var/run/docker.sock containernet/containernet /bin/bash
	ContainerID="$(docker ps -aqf 'name=FrontendServer')"
	gnome-terminal -x bash -c "docker exec -it '$ContainerID' cd /containernet/MaxiNet/ && make install && MaxiNetFront"

	for ((i=1; ((i<=$nrWorkers)); i++)); do

		docker run -d --name "Containernet-$i" --network ESLE_Network -it --mount source=ESLE_Volume,target=/containernet --rm --privileged --pid='host' -v /var/run/docker.sock:/var/run/docker.sock containernet/containernet /bin/bash
		ContainerID="$(docker ps -aqf 'name='Containernet-$i'')"
		gnome-terminal -x bash -c "docker exec -it '$ContainerID' cd /containernet/MaxiNet && make install"

	done

exit
