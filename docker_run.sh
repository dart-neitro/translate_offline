#!/bin/bash
echo "go to directory"
cd "$(pwd)"

echo "start container"

docker run -it -d \
    -p 3032:3032 \
    --env WORK_PORT=3032 \
    --env MONGODB_HOST=$DOCKER_LOCALHOST_IP \
    --env MONGODB_PORT=27017 \
    --volume "$(pwd)"/application:/app \
    translate_offline 


 
