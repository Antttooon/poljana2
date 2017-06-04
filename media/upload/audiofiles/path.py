import os

name_path = os.getcwd()
name_files = os.listdir(name_path)
for i in name_files:

    path = os.path.join(name_path, i)

    print(path)