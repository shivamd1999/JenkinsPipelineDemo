pipeline {
    agent any

    stages {
        stage('Python') {
            steps {
                bat "python hello1.py"
            }
        }
        stage('batch') {
            steps {
                sh "hello.bat"
            }
        }
        stage('build') {
            steps {
                echo ' World'
            }
        }
    }
}
