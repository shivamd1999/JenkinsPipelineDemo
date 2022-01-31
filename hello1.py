import os
import time
path = 'D:\shivamdubey'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
files.reverse()

for file in files[5:]:
    os.remove(os.path.join(path,file))

latest = files[:5]
print("Latest:", latest)

import os 
import zipfile
working_folder = 'D:\shivamdubey'
files = os.listdir(working_folder)
ZipFile = zipfile.ZipFile("python.zip", "w" )
for a in files:
    ZipFile.write(os.path.basename(a), compress_type=zipfile.ZIP_DEFLATED)
ZipFile.close()
