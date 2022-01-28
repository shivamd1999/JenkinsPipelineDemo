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
    
import os
import shutil
from zipfile import ZipFile
from os import path
from shutil import make_archive

    # Check if file exists
       if path.exists("D:\projects"):
    # get the path to the file in the current directory
        src = path.realpath("D:\projects");
    # rename the original file
        os.rename("career.guru99.txt","D:\projects")
    # now put things into a ZIP archive
        root_dir,tail = path.split(src)
        shutil.make_archive("guru99 archive","zip",root_dir)
    # more fine-grained control over ZIP files
        with ZipFile("D:\projects", "w") as newzip:
            newzip.write("D:\projects")
            newzip.write("D:\projects")
