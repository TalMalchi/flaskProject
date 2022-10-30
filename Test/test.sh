#!/usr/bin/bash

# ------- This Script desployes the project to test and production servers -------

# Variables
USER="ec2-user"
HOME_DIR="/home/ec2-user"
SECRET_KEY="/home/ec2-user/.ssh/id_dsa"
PROJECT_PATH="/var/lib/jenkins/workspace/*"
machine=$1


# First- check if the machine is empty, and then if test or production
# Test- deploy to test server. Copy all the files from jenkins workspace to test server and do `docker-compose build` and `docker-compose up`
# Then do curl to 127.0.0.1 to check if the application is running.
# Production- deploy to production server. Copy all the files from jenkins workspace to production server and do docker compose up

# check if machineis empty
if [ -z "$machine" ]
then
    echo "Please enter the machine name"
    exit 1
fi

# Deploy to test server and check if the application is running
if [ $machine == "test" ]
then
    echo "Deploying to test server"
    scp -i $SECRET_KEY -r $PROJECT_PATH ec2-user@test:~
    ssh -i $SECRET_KEY $USER@$machine "cd $HOME_DIR/Flask-app-AWS && docker-compose build"
    ssh -i $SECRET_KEY $USER@$machine "cd $HOME_DIR/Flask-app-AWS && docker-compose up -d"
    curl http://localhost:5005
    ssh -i $SECRET_KEY $USER@$machine "cd $HOME_DIR/Flask-app-AWS && docker-compose down"
elif [ $machine == "production" ]

# Deploy to production server and run the application
then
    echo "Deploying to production server"
    scp -i $SECRET_KEY -r $PROJECT_PATH ec2-user@prod:~
    ssh -i $SECRET_KEY $USER@$machine "cd $HOME_DIR/Flask-app-AWS && docker-compose up"
else
    echo "Invalid machine"
fi


