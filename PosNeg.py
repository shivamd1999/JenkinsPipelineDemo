txt_file = open("input.txt", "r")
file_content = txt_file.read()
print("The file content are: ", file_content)

list = file_content.split(",")
txt_file.close()
print("The list is: ", list)

try:
    P = open("C:\\Users\\shivamd1\\Positive.txt","w")  
    N = open("C:\\Users\\shivamd1\\Negative.txt","w")
    
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
