pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                sh """
                    docker-compose build -t talmalchi/Flask-App:latest .
                """
            }
        }
        stage('Login'){
            steps{  
                sh """
                    echo $DOCKERHUB_CREDETIALS_PSW | docker login --username $DOCKERHUB_CREDETIALS_USR --password-stdin
                """

            }


        }
        stage('Push'){
            steps{
                sh """
                    docker push talmalchi/Flask-App:latest
                """
            }
        }
        stage('Test'){
            steps{
                echo 'Testing...'
            }
        }
        stage('Deploy'){
            steps{
                echo 'Deploying...'
            }
        }
    }
    
}
