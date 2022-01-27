import os 
import datetime
import glob
path = 'D:\projects'

today = datetime.datetime.today()
os.chdir(path)

for root,directories,files in os.walk(path,topdown=False): 
    for name in files:
        t = os.stat(os.path.join(root, name))[10]
        filetime = datetime.datetime.fromtimestamp(t) - today


        if filetime.days <= -7:
            print(os.path.join(root, name), filetime.days)
            os.remove(os.path.join(root, name))

