pipeline {
    agent any

    stages {
        stage('Python') {
            steps {
                bat "python hello.py"
            }
        }
        stage('Hello') {
            steps {
                echo 'Hello '
            }
        }
        stage('build') {
            steps {
                echo ' World'
            }
        }
    }
}
