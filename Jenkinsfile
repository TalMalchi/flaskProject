pipeline{
    agent any
    environment{
        dockerhub=credentials('dockerhub')
        
    }
    stages{
        stage('Build'){
            
            steps{
                sh """
                    echo 'Building...'
                    docker build -t talmalchi/flaskapp:latest BackEnd/
                """
            }
        }
        stage('Login'){
            
            steps{  
                sh """
                    echo 'Login To DockerHub...'
                    echo $dockerhub_PSW | docker login -u $dockerhub_USR --password-stdin
                """

            }


        }
        stage('Push'){
            
            steps{
                
                sh """
                    echo 'Pushing To DockerHub...'
                    docker push talmalchi/flaskapp:latest
                    docker rmi talmalchi/flaskapp:latest #CHECK THIS

                    
                """
            }
        }
        stage('Test'){
            echo 'Testing...'
            steps{ 
                sh"""
                    echo 'Testing...'
                    bash -x deploy.sh test
            
                """
                // sshagent(['jenkins_ssh']) {
                //     sh """
                //         ssh -o StrictHostKeyChecking=no -i /var/lib/jenkins/.ssh/id_rsa
                //         bash -x deploy.sh test
                //     """
                // }     
                
            }
        }
        stage('Deploy'){
            
            steps{
                
                sh """
                    echo 'Deploying...'
                    chmod +x deploy.sh
                    bash -x deploy.sh prod
                """
            }
        }
    }
    
}

