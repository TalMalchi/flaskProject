pipeline{
    agent any
    environment{
        dockerhub=credentials('dockerhub')
        
    }
    stages{
        stage('Build'){
            echo 'Building...'
            steps{
                sh """
                    docker build -t talmalchi/flaskapp:latest BackEnd/
                """
            }
        }
        stage('Login'){
            echo 'Login To DockerHub...'
            steps{  
                sh """
                    echo $dockerhub_PSW | docker login -u $dockerhub_USR --password-stdin
                """

            }


        }
        stage('Push'){
            echo 'Pushing To DockerHub...'
            steps{
                
                sh """
                    docker push talmalchi/flaskapp:latest
                    docker rmi talmalchi/flaskapp:latest #CHECK THIS

                    
                """
            }
        }
        stage('Test'){
            echo 'Testing...'
            steps{      
                sh """
                    bash -x deploy.sh test
                """
            }
        }
        stage('Deploy'){
            echo 'Deploying...'
            steps{
                
                sh """
                    chmod +x deploy.sh
                    bash -x deploy.sh prod
                """
            }
        }
    }
    
}

