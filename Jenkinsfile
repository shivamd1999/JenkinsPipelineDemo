pipeline {
    environment {
        doError = '1'
    }
    agent any
        stages {
        stage('Bulding') {
            steps {
                bat 'PosNeg.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying'
            }
        }
        stage('Error') {
            when {
                expression { doError == '1' }
            }
            steps {
                echo "Failure"
                error "failure test."
            }
        }
        stage('Success') {
            when {
                expression { doError == '0' }
            }
            steps {
                echo "OK"
            }
        }
    }
    post {
        always {

                echo 'Status of build'
                emailext attachLog:true,
                subject: "Jenkins Pipeline Build Status",

                body:"${currentBuild.currentResult}: Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\n ${currentBuild.currentResult}: Job ${env.JOB_NAME} \n ${currentBuild.currentResult}: ${env.BUILD_TAG}",

                to:'dubeyshivam264@gmail.com'
        }
    }
}
