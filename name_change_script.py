"""It changes all filenames to their value minus 3001. So Instance3001.csv becomes Instance0.csv, etc."""

import os

def replace(folder_path):
    for path, subdirs, files in os.walk(folder_path):
        for name in files:
            if("set_cover_" in name):
                num = int(name[10:14])-3001
                file_path = os.path.join(path,name)
                new_name = os.path.join(path,"set_cover_"+str(num)+".txt")
                print("renaming",file_path,"to",new_name)
                os.rename(file_path, new_name)

replace('./set_cover')
