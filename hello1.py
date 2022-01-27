import os, time

path = "D:\projects"
now = time.time()

for filename in os.listdir(path):
    filestamp = os.stat(os.path.join(path, filename)).st_mtime
    filecompare = now - 1 * 86400
    if  filestamp < filecompare:
     print(filename)
