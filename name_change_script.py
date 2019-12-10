"""It changes all filenames to their value minus 3001. So Instance3001.csv becomes Instance0.csv, etc."""

import os

def replace(folder_path):
    for path, subdirs, files in os.walk(folder_path):
        for name in files:
            if("Instance" in name):
                num = int(name[8:12])-3001
                file_path = os.path.join(path,name)
                new_name = os.path.join(path,"Instance"+str(num)+".csv")
                print("renaming",file_path,"to",new_name)
                os.rename(file_path, new_name)

replace('.')
