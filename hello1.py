import os
import time

path = 'D:\hello'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
oldest = files[0-4]
newest = files[-1]

print("Oldest:", oldest)
print("Newest:", newest)
print("all by modified older to newest:",files)

