SHOW docker0 ip:
docker network inspect bridge --format='{{json .IPAM.Config}}'


SET 
export DOCKER_LOCALHOST_IP=172.17.0.1
