import os
def rename_files():
    #get file names from folder
    file_list = os.listdir(r"/Users/vypatz/Desktop/alphabet1")
    #print(file_list)
    saved_path = os.getcwd()
    print("cwd is " + saved_path)
    os.chdir(r"/Users/vypatz/Desktop/alphabet1")

    #for each file, rename filename
    remove_these = dict((ord(char), None) for char in '0123456789')
    for file_name in file_list:
        os.rename(file_name, file_name.translate(remove_these))
    os.chdir(saved_path)

rename_files()
    
