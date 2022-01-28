import os 
import datetime
path = 'D:\hello'

today = datetime.datetime.today()
os.chdir(path)

for root,directories,files in os.walk(path,topdown=False): 
    for name in files:
        t = os.stat(os.path.join(root, name))[8]
        filetime = datetime.datetime.fromtimestamp(t) - today


        if filetime.days <= -18:
            print(os.path.join(root, name), filetime.days)
            os.remove(os.path.join(root, name))
            
# importing ZipFile class from zipfile module
from zipfile import ZipFile

# specifying the zip file_name
file = "D:\hello"

# opening the zip file in READ mode
with ZipFile(file, 'r') as zip:
    # to get a list containing a ZipInfo object
    print(zip.getinfo("test"))

            
