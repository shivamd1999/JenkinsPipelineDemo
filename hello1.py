import os, glob, time
root = 'D:\fliker'
date_file_list = []
for folder in glob.glob(root):
    print('folder =', folder)
    
    for file in glob.glob(folder + 'D:\fliker'):
       
        stats = os.stat(file)
        
        lastmod_date = time.localtime(stats[8])
       
        date_file_tuple = lastmod_date, file
        date_file_list.append(date_file_tuple)


date_file_list.sort()
date_file_list.reverse() 
print("%-40s %s" % ("filename:", "last modified:"))
for file in date_file_list:
   
    folder, file_name = os.path.split(file[1])
   
    file_date = time.strftime("%m/%d/%y %H:%M:%S", file[0])
    print("%-40s %s" % (file_name, file_date))
