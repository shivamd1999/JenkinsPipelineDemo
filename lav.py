def  funargs(*args)
    print(args[0]))
    
har = ["${env.BUILD_NUMBER}","${env.JOB_NAME}","${env.BUILD_URL}]
funargs(*har)








