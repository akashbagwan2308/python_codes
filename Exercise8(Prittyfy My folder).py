# # Oh soldier prettify my folder
# path as input
# directory
# format
# C://  harry.txt   jpg

import os
def soldier(path, file,format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")
    for file in files:
        if file not in files:
            os.rename(file,file.capitalize())
        if os.path.splitext(file)[1] == format:
            os.rename(file,f"Screenshot{i}{format}")
            i+=1

soldier(r"C:\Users\Lenovo\OneDrive\Pictures\Screenshots",
        r"C:\Users\Lenovo\PycharmProjects\firstProgram\Akash.txt", ".png")