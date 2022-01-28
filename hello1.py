import os 
import datetime
path = 'D:\projects'

today = datetime.datetime.today()
os.chdir(path)

for root,directories,files in os.walk(path,topdown=False): 
    for name in files:
        t = os.stat(os.path.join(root, name))[8]
        filetime = datetime.datetime.fromtimestamp(t) - today


        if filetime.days <= -18:
            print(os.path.join(root, name), filetime.days)
            os.remove(os.path.join(root, name))
            
 
for dirpath,dirnames,filenames in os.walk(path):
    print("current path",dirpath)
    print("current directories",dirnames)
    print("The Remaining files are:",filenames)
    
from zipfile
import ZipFile
  
# specifying the zip file name
file_name = "D:\projects"
  
# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()
  
    # extracting all the files
    print('Extracting all the files now...')
    zip.extractall()
    print('Done!')
