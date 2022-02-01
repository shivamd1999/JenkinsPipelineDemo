import os
import time
import json
with open('file.json') as f:
    data = json.load(f)
    
print data

os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
files.reverse()

for file in files[5:]:
    os.remove(os.path.join(path,file))

latest = files[:5]
print("Latest:", latest)

import zipfile

files = os.listdir(working_folder)
ZipFile = zipfile.ZipFile("Saved.zip", "w" )
for a in files:
    ZipFile.write(os.path.basename(a), compress_type=zipfile.ZIP_DEFLATED)
ZipFile.close()
