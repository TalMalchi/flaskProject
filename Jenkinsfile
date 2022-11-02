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
            steps{ 
                // sh"""
                //     echo 'Testing...'
                //     bash -x deploy.sh test
            
                // """
                sshagent(credentials : ['jenkins_ssh']) {
                    sh """
                        echo 'Testing...'
                        scp -i /home/ec2-user/.ssh/id_dsa -r /var/lib/jenkins/workspace/* ec2-user@test:~
                        ssh -i /home/ec2-user/.ssh/id_dsa ec2-user@test 
                        bash -x deploy.sh test
                    """
                }     
                
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

