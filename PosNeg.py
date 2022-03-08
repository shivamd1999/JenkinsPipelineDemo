input_string = input("Enter a list element separated by space \n")
list  = input_string.split()
try:
    P = open("C:\\Users\\shivamd1\\Desktop\\Positive.txt","w")  
    N = open("C:\\Users\\shivamd1\\Desktop\\Negative.txt","w")
    
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
