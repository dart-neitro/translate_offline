#!/bin/bash

echo "goto app";
cd /app;
echo "start gunicorn";
# gunicorn -w 1 -b :3031 run_gunicorn:app ;
# echo "gunicorn -w 4 -b 0.0.0.0:80 run_gunicorn:app" > /run/start.sh
echo "port: $WORK_PORT"
echo $WORK_PORT 
gunicorn -w 1 -b 0.0.0.0:$WORK_PORT run_gunicorn:app
