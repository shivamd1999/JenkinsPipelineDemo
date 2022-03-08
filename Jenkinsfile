pipeline {
    agent any

    stages {
        stage('Input') {
            steps {
                input('Do you want to proceed?')
            }
        }
        stage('build') {
            steps {
                input_string = input("Enter a list element separated by space \n")
list  = input_string.split()
try:
    P = open("Positive.txt","w")  
    N = open("Negative.txt","w")
    
    for num in list:
        try:
            if int(num) >= 0:
                P.write(str(num))
                P.write('\n')
            else:
                N.write(str(num))
                N.write('\n')
        except ValueError:
            print("Invalid number")
            
finally:
    P.close()
    N.close()
            }
        }

        stage('If Proceed is clicked') {
            steps {
                print('hello')
            }
        }
    }
}
