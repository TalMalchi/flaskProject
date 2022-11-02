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
                        [ -d ~/.ssh ] || mkdir ~/.ssh && chmod 0700 ~/.ssh
                        ssh-keyscan -t rsa test >> ~/.ssh/known_hosts
                        echo 'Testing...'
                        bash -x deploy.sh test
                        """

                    
                   
                }          
            }
        }
        stage('Deploy'){
            
            steps{
                sshagent(credentials:['ec2-user-prod']) {
                    sh """
                        echo 'Deploying...'
                        bash -x deploy.sh prod
                    """
            }
        }
    }
    
}

}