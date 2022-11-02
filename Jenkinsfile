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
                sshagent(credentials:['ec2-user-test']) {
                    sh """
                        echo 'Testing...'
                        bash -x deploy.sh
                        """
                    
                   
                }          
            }
        }
        stage('Deploy'){
            
            steps{
                sshagent(credentials:['ec2-user-prod']) {
                    sh """
                        echo 'Deploying...'
                        chmod +x deploy.sh
                        bash -x deploy.sh prod
                    """
            }
        }
    }
    
}

}