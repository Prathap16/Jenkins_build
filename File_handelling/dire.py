import os,sys
dirs=[]
files=[]
dir_path=input("Enter Directory path:")
print(dir_path)
if os.path.isdir(dir_path):
    print("Path:",dir_path)
    print("lsting dir:",os.listdir(dir_path))
    os.chdir(dir_path)
    cwd=os.getcwd()
    print(cwd)
    for name in os.listdir(cwd):
        if os.path.isdir(name):
            dirs.append(name)
        if os.path.isfile(name):
            files.append(name)
    print("Direoryes present in",cwd,dirs)
    print("files present in", cwd, files)
else:
    print(dir_path,"does not exists. please check!")
