import os
import time

path = 'D:\hello'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
oldest = files[0]
newest = (files[-1],files[-2],files[-3],files[-4],files[-5])

print("Oldest:", oldest)
print("Newest:", newest)
print("all by modified older to newest:",files)

