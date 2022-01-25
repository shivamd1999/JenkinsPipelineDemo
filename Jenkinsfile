pipeline {
    agent any

    stages {
        stage('build') {
            dir("build_folder"){
                bat "run_build_window.bat"
            }
        }
    }
}
