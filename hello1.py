import os 
import datetime
import glob
path = 'D:\shivam'

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
from pathlib import Path
from zipfile import ZipFile
DOWNLOAD_DIR = Path("D:\shivam")
ZIPPED_FILE_DIR = Path("D:\shivam")
def get_list_of_all_folders(download_dir: Path):
	return [f for f in download_dir.iterdir() if download_dir.is_dir()]
def zip_files():
	folder_list = get_list_of_all_folders(DOWNLOAD_DIR)
	with ZipFile(ZIPPED_FILE_DIR / "my_zip.zip", "w") as zip:
		for folder in folder_list:
			zip.write(folder)
			zip_files()

