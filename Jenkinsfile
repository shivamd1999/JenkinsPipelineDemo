pipeline {
    agent { docker { image 'python:3.10.1-alpine'} }

    stages {
        stage('build') {
            steps {
               sh 'python --version'
                
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'
            }
        }
        stage('Release') {
            steps {
                echo 'Releasing'
            }
        }
    }
}
