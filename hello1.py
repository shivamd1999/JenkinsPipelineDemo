import os 
import datetime
path = 'D:\projects'

today = datetime.datetime.today()
os.chdir(path)

for root,directories,files in os.walk(path,topdown=False): 
    for name in files:
        t = os.stat(os.path.join(root, name))[8]
        filetime = datetime.datetime.fromtimestamp(t) - today


        if filetime.days <= -39:
            print(os.path.join(root, name), filetime.days)
            os.remove(os.path.join(root, name))
            
 
for dirpath,dirnames,filenames in os.walk(path):
    print("current path",dirpath)
    print("current directories",dirnames)
    print("The Remaining files are:",filenames)
    
