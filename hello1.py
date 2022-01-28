import os
import time

path = 'D:\hello'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
new = files[5]

print(new)

