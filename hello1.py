import os
import time

path = 'D:\hello'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest = (files[-1],files[-2],files[-3],files[-4],files[-5])

print("Newest:", newest)
print("all by modified older to newest:",files)

