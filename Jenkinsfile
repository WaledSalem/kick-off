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
        stage('Deploy'){
            steps{
                sh './scripts/deploy.sh'
            }
        }                   
        stage('Loadbalance'){
            steps{
                sh './scripts/nginx.sh'
            }
        }
    }
}