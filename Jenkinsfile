pipeline {
    agent any
    stages{ 
        stage('DBuild'){
            steps{
                sh './dscripts/dbuild.sh'
            }
        }
        stage('DDeploy'){
            steps{
                sh './scripts/ddeploy.sh'
            }
        }                   
        stage('DLoadbalance'){
            steps{
                sh './dscripts/dnginx.sh'
            }
        }
    }
}