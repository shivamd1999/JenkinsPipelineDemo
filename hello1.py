import glob
import os

list_of_files = glob.glob('D:\fliker') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)

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

