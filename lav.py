import os

print(os.environ["The Jobs name is:",'JOB_NAME'])
print(os.environ['BUILD_NUMBER'])
print(os.environ['BUILD_URL'])
print(os.getenv.get['BUILD_DURATION'])
print(os.environ['BUILD_TAG'])

# from datetime import datetime
# now = datetime.now()
# print (now.strftime("%Y-%m-%d %H:%M:%S"))

# def  funargs(*args):
#     for item in args:
#         print(item)
    
# har = ["${currentBuild.currentResult}: Job ${JOB_NAME} build ${BUILD_NUMBER}\n ${currentBuild.currentResult}: Job ${JOB_NAME} \n ${currentBuild.currentResult}: ${BUILD_TAG}"]
# funargs(*har)
# pipeline{
#     agent any
    
#     stages{
#         stage("Build number "){
#             steps{
#                 echo "The build number is ${env.BUILD_NUMBER}"                                              
#             }
#         }
#         stage("Jobs Name"){
#             steps{
#                 echo "The Jobs name is ${env.JOB_NAME}"                                              
#             }
#         }
#         stage("Build URL"){
#             steps{
#                 echo "The Build URL is ${env.BUILD_URL}"                                               
#             }
#         }
#         stage("Dates"){
#             steps{
#                 echo "The Updated date ${new Date()}"                                                
#             }
#         }
#         stage("Build Duration"){
#             steps{
#                 echo "The Build Duration is  ${currentBuild.durationString}"                                               
#             }
#         }
#     }     
# }





