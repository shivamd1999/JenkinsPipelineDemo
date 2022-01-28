import glob
import os

folder_path = "D:\fliker"
files_path = os.path.join(folder_path, 'D:\fliker')
files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
print (files[0],files[1])
