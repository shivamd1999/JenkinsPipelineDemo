def  funargs(*args):
    for item in args:
        print(item)
    
har = ["${currentBuild.currentResult}: Job ${JOB_NAME} build ${BUILD_NUMBER}\n ${currentBuild.currentResult}: Job ${JOB_NAME} \n ${currentBuild.currentResult}: ${BUILD_TAG}"]
funargs(*har)








