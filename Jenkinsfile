pipeline {
    agent any
        stages {
        stage('Bulding') {
            steps {
                bat 'Jenkinsemail.py'
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
