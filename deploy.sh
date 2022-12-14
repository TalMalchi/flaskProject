#!/usr/bin/bash

## This Script desployes the project to test and production servers 

#Variables
USER="ec2-user"
HOME_DIR="/home/ec2-user"
SECRET_KEY="/var/lib/jenkins/.ssh/id_dsa"
machine=$1


## First- check if the machine is test or production
# Test- deploy to test server. Copy all the files from jenkins workspace to test server and do `docker-compose build` and `docker-compose up`
# Then do curl to 127.0.0.1 to check if the application is running.
# Production- deploy to production server. Copy all the files from jenkins workspace to production server and do docker compose up

#check if input is empty, then check if it is test or production
if [ -z "$machine" ]; then
    echo "Please enter test or production"
    exit 1

elif [ $machine == "test" ]
then
    echo "Deploying to test server"
    scp -o StrictHostKeyChecking=no -r /var/lib/jenkins/workspace/* ec2-user@test:~
    ssh -o StrictHostKeyChecking=no $USER@test "cd $HOME_DIR/Flask-app-AWS && docker pull talmalchi/flaskapp:latest && docker-compose up -d && curl http://localhost:5005 "
    # ssh -o StrictHostKeyChecking=no $USER@test "cd $HOME_DIR/Flask-app-AWS && docker-compose build && docker-compose up -d && curl http://localhost:5005 && docker-compose down"
    
elif [ $machine == "prod" ]
then
    echo "Deploying to production server"
    scp -o StrictHostKeyChecking=no -r /var/lib/jenkins/workspace/* ec2-user@prod:~
    ssh -o StrictHostKeyChecking=no $USER@test "cd $HOME_DIR/Flask-app-AWS && docker pull talmalchi/flaskapp:latest && docker-compose up -d "
    #ssh -o StrictHostKeyChecking=no $USER@prod "cd $HOME_DIR/Flask-app-AWS && docker-compose up -d"
else
    echo "Invalid machine"
fi


