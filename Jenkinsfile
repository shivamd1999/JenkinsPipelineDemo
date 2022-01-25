pipeline {
    agent { docker { image 'Python 3.9.5-alpine'} }

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
