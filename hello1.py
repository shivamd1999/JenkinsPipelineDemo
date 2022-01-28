import os 
import datetime
path = 'D:\PythonDemo'

today = datetime.datetime.today()
os.chdir(path)

for root,directories,files in os.walk(path,topdown=False): 
    for name in files:
        t = os.stat(os.path.join(root, name))[8]
        filetime = datetime.datetime.fromtimestamp(t) - today


        if filetime.days <= -18:
            print(os.path.join(root, name), filetime.days)
            os.remove(os.path.join(root, name))
            
import os
import zipfile

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

if __name__ == '__main__':
    zipf = zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('D:\PythonDemo', zipf)
    zipf.close()
