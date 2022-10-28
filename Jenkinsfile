pipeline{
    agent any
    environment{
        dockerhub=credentials('dockerhub')
        
    }
    stages{
        stage('Build'){
            steps{
                sh """
                    docker-compose build -t talmalchi/flaskapp:latest . 
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
