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
            
import zipfile
target = 'D:\hello'
handle = zipfile.ZipFile('D:\hello','w')
handle.write(target, compress_type = zipfile.ZIP_DEFLATED)
handle.close()
