#!/usr/bin/bash

## This Script desployes the project to test and production servers 

#Variables
USER="ec2-user"
HOME_DIR="/home/ec2-user"
machine=$1


## First- check if the machine is test or production
# Test- deploy to test server. Copy all the files from jenkins workspace to test server and do `docker-compose build` and `docker-compose up`
# Then do curl to 127.0.0.1 to check if the application is running.
# Production- deploy to production server. Copy all the files from jenkins workspace to production server and do docker compose up


if [ $machine == "test" ]
then
    echo "Deploying to test server"
    sudo scp -i /home/ec2-user/.ssh/id_dsa -r /var/lib/jenkins/workspace/* ec2-user@test:~
    sudo ssh -i /home/ec2-user/.ssh/id_dsa $USER@$machine "cd $HOME_DIR/Flask-app-AWS && docker-compose build"
    sudo ssh -i /home/ec2-user/.ssh/id_dsa $USER@$machine "cd $HOME_DIR/Flask-app-AWS && docker-compose up -d"
    curl http://localhost:5005
elif [ $machine == "production" ]
then
    echo "Deploying to production server"
    scp -i /home/ec2-user/.ssh/id_dsa -r /var/lib/jenkins/workspace/* ec2-user@prod:~
    ssh -i /home/ec2-user/.ssh/id_dsa $USER@$machine "cd $HOME_DIR/Flask-app-AWS && docker-compose up"
else
    echo "Invalid machine"
fi


