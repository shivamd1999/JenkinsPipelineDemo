pipeline {
    agent any

    stages {
        stage('Input') {
            steps {
                input('Do you want to proceed?')
            }
        }
        stage('build') {
            steps {
                bat "PosNeg.py"
            }
        }

        stage('If Proceed is clicked') {
            steps {
                print('hello')
            }
        }
    }
}
