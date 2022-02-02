import json
import time
import zipfile
import os
try:
    with open('file.json','r') as filesdata:
        filedata=json.load(filesdata)   
    list_of_files = filter( lambda x: os.path.isfile(os.path.join(filedata['path'], x)),
                            os.listdir(filedata['path']))

    list_of_files = sorted( list_of_files,
                            key = lambda x: os.path.getmtime(os.path.join(filedata['path'], x)))
    fileno=filedata['files']
    list_of_files.reverse()
    print("The Update Files are:")
    for index, file in enumerate(list_of_files):
        if index > (fileno-1):
            os.remove(os.path.join(filedata['path'],file))
        else:
            file_path = os.path.join(filedata['path'], file)
            timestamp_str = time.strftime('%d/%m/%Y :: %H:%M:%S',
                                    time.gmtime(os.path.getmtime(file_path)))
            print(timestamp_str, ' -->', file)

    path=filedata['path']
    def prepare_zip(path):
        new_file = filedata['path']+'.zip'
        
        zip = zipfile.ZipFile(new_file, 'w', zipfile.ZIP_DEFLATED)
        
        for dir_file, dir_names, files in os.walk(filedata['path']):
            f_path = dir_file.replace(dir_file, '')
            f_path = f_path and f_path + os.sep
            
            for file in files:
                zip.write(os.path.join(filedata['path'], file), f_path + file)
        zip.close()
        print("Files Zipped successfully..")
        return os.rename(new_file,filedata['working_folder'])

    prepare_zip(filedata['path'])
except FileExistsError:
    print("File Already Exist.")
                                                                      
