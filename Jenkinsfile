pipeline{
    agent any
    environment{
        dockerhub=credentials('dockerhub')
        
    }
    stages{
        stage('Build'){
            steps{
                sh """
                    docker build -t talmalchi/flaskapp:latest BackEnd/
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
                    docker push talmalchi/flaskapp:latest
                """
            }
        }
        stage('Test'){
            steps{
                echo 'Testing...'
                sh """
                    docker-compose up
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
