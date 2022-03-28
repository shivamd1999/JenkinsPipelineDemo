def  funargs(*args):
    for item in args:
        print(item)
    
har = [${env.BUILD_NUMBER}, ${env.JOB_NAME}, ${env.BUILD_URL}]
funargs(*har)








