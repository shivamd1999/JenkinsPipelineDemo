pipeline {
    agent {lable 'Slave1'}
    stages {
        stage('Python') {
            steps {
                bat "hello1.py"
            }
        }
        stage('batch') {
            steps {
                bat "hello.bat"
            }
        }
        stage('build') {
            steps {
                echo ' World'
            }
        }
    }
}
