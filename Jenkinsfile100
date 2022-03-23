pipeline{
    agent any
    
    stages{
        stage("Build number "){
            steps{
                echo "The build number is ${env.BUILD_NUMBER}"
                echo "You can also use \${BUILD_NUMBER} -> ${BUILD_NUMBER}"                                                
            }
        }
        stage("Jobs Name"){
            steps{
                echo "The build number is ${env.JOB_NAME}"
                echo "You can also use \${JOB_NAME} -> ${JOB_NAME}"                                                
            }
        }
        stage("Build URL"){
            steps{
                echo "The build number is ${env.BUILD_URL}"
                echo "You can also use \${BUILD_URL} -> ${BUILD_URL}"                                                
            }
        }
        stage("Build Duration"){
            steps{
                echo "The build number is Current time ${new Date()}"
                echo "You can also use \${new Date()} -> ${new Date()}"                                                
            }
        }
        stage("Build ok"){
            steps{
                echo "The build number is Current time ${currentBuild.durationString}"
                echo "You can also use \${currentBuild.durationString} -> ${currentBuild.durationString}"                                                
            }
        }
    }     
}
