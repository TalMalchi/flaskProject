pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                sh """
                    docker-compose build --no-cache
                """
            }
        }
        stage('Run'){
            steps{
                sh """
                    docker-compose up -d
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
