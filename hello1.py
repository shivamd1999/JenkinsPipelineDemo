import os
import time
from pathlib import Path
from zipfile import ZipFile
path = 'D:\Projects'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
files.reverse()

for file in files[5:]:
    os.remove(os.path.join(path,file))

latest = files[:5]
print("Latest:", latest)

ZIPPED_FILE_DIR = Path('D:\Projects')

def get_list_of_all_folders(download_dir: Path):
    return [f for f in download_dir.iterdir() if download_dir.is_dir()]
def zip_files():
    folder_list = get_list_of_all_folders(ZIPPED_FILE_DIR)
    with ZipFile(ZIPPED_FILE_DIR / "Python.zip", "w") as zip:
        for folder in folder_list:
          zip.write(folder)

zip_files()
