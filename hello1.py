import os 

path = 'D:\fliker'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)

oldest = file[0]
newest = files[5]

print "Oldest:", oldest
print "Newest:", newest
print "All by modified oldest to newest:",files

import os
from pathlib import Path
from zipfile import ZipFile
DOWNLOAD_DIR = Path("D:\fliker")
ZIPPED_FILE_DIR = Path("D:\fliker")
def get_list_of_all_folders(download_dir: Path):
	return [f for f in download_dir.iterdir() if download_dir.is_dir()]
def zip_files():
	folder_list = get_list_of_all_folders(DOWNLOAD_DIR)
	with ZipFile(ZIPPED_FILE_DIR / "my_zip.zip", "w") as zip:
		for folder in folder_list:
			zip.write(folder)

zip_files()

