import os
import shutil

# folder_path = input("Enter the path to the read files: ")
# saving_path = input("Enter the path to the file that has the saving folder: ")

folder_path = r"C:\Users\ozan.akyel\Desktop\name_change"
saving_path = r"C:\Users\ozan.akyel\Desktop\name_change\result\try"


"""
create saving folder
but if This folver was already exists, script is checking.

"""

if not os.path.exists(saving_path):
    try:
        os.makedirs(saving_path)
        print(f"{saving_path} was created")
    except FileExistsError:
        print("can not created")
else:
    print("Directory " , saving_path ,  " already exists")


""" 
list for all items in source folder
replace some characters and keep as another object(if you want keep same object)
save all file to saving_path

"""

for i in os.listdir(folder_path):
    if i.endswith(".jpg") or i.endswith(".xml"):
        j=i.replace(" ", "")
        j=j.replace('(','_')
        j=j.replace(")","-")
        # os.rename(os.path.join(folder_path,i),os.path.join(saving_path,j))        # os.rename(old_name, new_name)   this is delete old_name and Create new_name
        shutil.copyfile(os.path.join(folder_path,i), os.path.join(saving_path,j))   # shutil.copyfile(source, target)   this is copy from source and save to target
        print(f"dosya {os.path.join(saving_path,j)} olarak kaydededildi")
    else:
        print(f"{i} degistirilmek istenen türde dosya değil")

