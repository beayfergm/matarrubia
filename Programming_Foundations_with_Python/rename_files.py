import os

myFolder = r"/Users/fernandomatarrubia/Desktop/example/prank"

def rename_files():
    file_list = os.listdir(myFolder)
    current_directory = os.getcwd()
    os.chdir(myFolder)
    for file_name in file_list:
        newFileName = file_name.translate(None, "0123456789")
        print("Old Name - "+file_name+". New Name - "+newFileName)
        os.rename(file_name, newFileName)
    os.chdir(current_directory)

rename_files()
