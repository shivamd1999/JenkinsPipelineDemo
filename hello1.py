import os
import time
from pathlib import Path
from zipfile import ZipFile
path = 'D:\shivamdubey'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
files.reverse()

for file in files[5:]:
    os.remove(os.path.join(path,file))

latest = files[:5]
print("Latest:", latest)

ZIPPED_FILE_DIR = Path('D:\Projects')

working_folder = 'D:\shivamdubey'
files = os.listdir(working_folder)
ZipFile = zipfile.ZipFile("python.zip", "w" )
for a in files:
    ZipFile.write(os.path.basename(a), compress_type=zipfile.ZIP_DEFLATED)
ZipFile.close()
