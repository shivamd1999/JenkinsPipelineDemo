import os
import time

path = 'D:\fliker'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
new = files[-1]

print(new)

