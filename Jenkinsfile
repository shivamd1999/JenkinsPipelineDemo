pipeline {
    agent any

    stages {

        stage("Interactive_Input") {
            steps {
                script {
                def userInput = input(
                 id: 'userInput', message: 'Enter path of test reports:?', 
                 parameters: [
                 [$class: 'TextParameterDefinition', defaultValue: 'None', description: 'Path of config file', name: 'Config'],
                 ])
                echo ("IQA Sheet Path: "+userInput['Config'])
                }
            }
        }
    }
}

