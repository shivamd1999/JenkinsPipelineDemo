def my_function(the):
    print(the + "")
my_function(" build number is ${env.BUILD_NUMBER}")
my_function("build number is ${env.JOB_NAME}")
my_function("build number is ${env.BUILD_URL}")
