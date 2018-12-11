docker stop $(docker ps -a -q)
docker service rm $(docker service ls -q)
