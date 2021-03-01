pipeline {
    agent any 
    stages{
        stage('Test'){
            steps{
                sh './scripts/test.sh'
            }
        }
        stage('Ansible'){
            steps{
                sh './scripts/ansible.sh'
            }
        }
        stage('Build'){
            steps{
                sh './scripts/build.sh'
            }
        }
        stage('Push'){
            steps{
                withDockerRegistry(credentialsId: 'docker-hub-credentials', url: 'https://index.docker.io/v1/'){
                    image.push
                }
            }
        }
        stage('Deploy'){
            steps{
                sh './scripts/deploy.sh'
            }
        }                   
    }
}
