import os
import shutil
source=input("Enter Source Folder Name")
destination=input("Enter Destination Folder")
source=source+'/'
destination=destination+'/'
list=os.listdir(source)
for file in list:
    shutil.copy((source+file),destination)

