#!/bin/bash

echo "stop docker images"
docker stop $(docker ps -q --filter ancestor="translate_offline")
