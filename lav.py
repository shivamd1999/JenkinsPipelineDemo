pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                echo 'building'
            }
        }
        stage('test') {
            steps {
                echo 'Testing'
            }
        }
        stage('Moniter') {
            steps {
                echo 'monitering'
            }
        }
        stage('deploy') {
            steps {
                echo 'deploying'
            }
        }
    }
}
