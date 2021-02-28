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
        stage('Build-Images'){
            steps{
                sh './scripts/build-images.sh'
            }
        }
        stage('Deploy-Services'){
            steps{
                sh './scripts/deploy-services.sh'
            }
        }                   
    }
}