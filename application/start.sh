#!/bin/bash

echo "goto app";
cd /app;
echo "start gunicorn";
# gunicorn -w 1 -b :3031 run_gunicorn:app ;
# echo "gunicorn -w 4 -b 0.0.0.0:80 run_gunicorn:app" > /run/start.sh
gunicorn -w 4 -b 0.0.0.0:3031 run_gunicorn:app