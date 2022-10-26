pipeline{
    agent any
    enviroment{
        DOCKERHUB_CREDENTIALS=credentials('dockerhub')
        
    }
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
                    echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
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
