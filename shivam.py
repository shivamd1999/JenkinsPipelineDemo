
pipeline {
    agent any
    stages {
        stage('batch') {
            steps {
                bat "save1.bat"
            }
        }
    }
}
