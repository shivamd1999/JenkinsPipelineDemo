pipeline {
    agent any
    stages {
        stage('Wait for user to input text?') {
            steps {
                script {
                    def userInput = input(id: 'userInput', message: 'Merge to?',
                    parameters: [[$class: 'ChoiceParameterDefinition', defaultValue: 'strDef', 
                    description:'describing choices', name:'nameChoice', choices: "PosNeg.py"]
                    ])
                    
                    println(userInput); //Use this value to branch to different logic if needed
                }
            }
        }
    }
}
