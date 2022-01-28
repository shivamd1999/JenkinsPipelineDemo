import os
import time
path = 'D:\fliker'
l_files = os.listdir(path) 

for file in l_files:
 
 file_path = f'{path}\\{file}'
 if os.path.isfile(file_path):
  
  try:
   os.startfile(file_path, 'print')
   print(f'Printing {file}')
   time.sleep(5)
   
   
   except:
    print(f'ALERT: {file} could not be printed! Please check\the associated softwares, or the file type.')
  else:
   print(f'ALERT: {file} is not a file, so can not be printed!')
   print('Task finished!')
