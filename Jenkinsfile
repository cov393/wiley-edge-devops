pipeline {
    agent any
    stages{
        stage ('Clone repository'){
            steps{
                git 'https://github.com/cov393/wiley-edge-devops.git'
            }
        }
        stage ('Build'){
            steps{
                sh 'mvn clean install'
            }
        }
        stage('Run Tests'){
            steps{
                sh 'mvn test'
            }
        }
    }
}