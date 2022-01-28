import glob
import os

list_of_files = glob.glob('D:\fliker')
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)
