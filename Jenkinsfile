pipeline{
    agent any
    environment{
        dockerhub=credentials('dockerhub')
        
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
                    echo $dockerhub_PSW | docker login -u $dockerhub_USR --password-stdin
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
                sh """
                    bash -x Test/test.sh
                """
            }
        }
        stage('Deploy'){
            steps{
                echo 'Deploying...'
            }
        }
    }
    
}
