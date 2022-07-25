import os
import shutil
 
from PIL import Image

"""
###Sort func
Moves files into respective folders according to their extensions
"""


def resize(path):

    list_ = os.listdir(path)
    print(list_)
    os.chdir(path)
    crt = os.getcwd()
    print (crt)
	
    #Traverses to every file

    for filename in list_:
        name,ext = os.path.splitext(filename)
        print(f"working on {filename}")
        # ext = ext[1:]
        # if ext == '':
        #     continue
        # if os.path.exists(path+'/'+ext):
        #     shutil.move(path+'/'+filename, path+'/'+ext+'/'+filename)
        # else:
        #     os.makedirs(path+'/'+ext)
        #     shutil.move(path+'/'+filename, path+'/'+ext+'/'+filename)
        
        im = Image.open(path +'/'+filename)
        imR = im.resize((150,150), Image.ANTIALIAS)
        imR.save(path+'/'+filename, quality=100)

# resize("./lfw_data")

def delFolder(fPath):
    _, _, files = next(os.walk("/usr/lib"))
    file_count = len(files)

    os.chdir(fPath)
    dest_dir = os.getcwd()
    #generator that walks over the folder tree
    walker = os.walk(dest_dir)
    for data in walker:
        print(f"working on subdir: {data[0]}")


def resize2(path):
    #Set path as current working directory
    os.chdir(path)
    dest_dir = os.getcwd()
    #generator that walks over the folder tree
    walker = os.walk(dest_dir)
     
    # the first walk would be the same main directory
    # which if processed, is redundant
    # and raises shutil.Error
    # as the file already exists
     
    rem_dirs = walker
     
    for data in walker:
        print(f"working on subdir: {data[0]}")
        _, _, files = next(os.walk(f"{data[0]}"))
        file_count = len(files)
        if f"{data[0]}" != "/Users/ishaan/My_Projects/face_recog/lfw":
            if file_count <= 1:
                print(f"removing {data[0]}; it has only {file_count} file.")
                shutil.rmtree(f"{data[0]}")
        print(f"number of files: {file_count}")
    #     for files in data[2]:
    #         try:
    #             print(f"working on dir: {data[0]}")
    #             print(f"files: {files}")
    #             im = Image.open(data[0] + os.sep + files)
    #             imR = im.resize((150,150), Image.ANTIALIAS)
    #             imR.save(data[0] + os.sep + files, quality=100)
    #             # shutil.move(data[0] + os.sep + files, dest_dir)
    #             # print(data[0] + os.sep + files)
    #         except shutil.Error:
    # # to be on the safer side
    #             continue
# resize("lfw")

def make_test_data(fpath, tpath):
    #Set path as current working directory
    os.chdir(fpath)
    dest_dir = os.getcwd()
    #generator that walks over the folder tree
    walker = os.walk(dest_dir)
     
    # the first walk would be the same main directory
    # which if processed, is redundant
    # and raises shutil.Error
    # as the file already exists
     
    rem_dirs = walker
     
    for data in walker:
        print(f"working on subdir: {data[0]}")
        _, _, files = next(os.walk(f"{data[0]}"))
        file_count = len(files)
        print(f"FILE: {files}")
        if f"{data[0]}" != "/Users/ishaan/My_Projects/face_recog/lfw":
            if file_count >= 2:
                print(f"removing {data[0]}; it has only {file_count} file.")
                # shutil.rmtree(f"{data[0]}")
                shutil.copy(data[0] + os.sep + files, tpath)
                continue
        print(f"number of files: {file_count}")
    #     for files in data[2]:
    #         try:
    #             print(f"working on dir: {data[0]}")
    #             print(f"files: {files}")
    #             im = Image.open(data[0] + os.sep + files)
    #             imR = im.resize((150,150), Image.ANTIALIAS)
    #             imR.save(data[0] + os.sep + files, quality=100)
    #             # shutil.move(data[0] + os.sep + files, dest_dir)
    #             # print(data[0] + os.sep + files)
    #         except shutil.Error:
    # # to be on the safer side
    #             continue
# resize("lfw")

def extract(fpath, tpath):
    #Set path as current working directory
    os.chdir(fpath)
    dest_dir = os.getcwd()
    # print(f"cwd: {dest_dir}")
    #generator that walks over the folder tree
    walker = os.walk(dest_dir)
     
    # the first walk would be the same main directory
    # which if processed, is redundant
    # and raises shutil.Error
    # as the file already exists
    
    rem_dirs = walker
    
    for data in walker:
        # print(data)
        filesN = (len(data[2]))
        testN = filesN // 2
        files = data[2]
        # print(data[2])
        for i in range(testN):
            try:
                # print(os.getcwd())
                # continue
                shutil.move(data[0] + os.sep + files[i], tpath)  
                print(f"{data[0] + os.sep + files[i]} moved to {tpath}")
            except shutil.Error:
    # to be on the safer side
                print("ERROR!")
                continue

def view_files(fpath):
    #Set path as current working directory
    os.chdir(fpath)
    dest_dir = os.getcwd()
    # print(f"cwd: {dest_dir}")
    #generator that walks over the folder tree
    walker = os.walk(dest_dir)
     
    # the first walk would be the same main directory
    # which if processed, is redundant
    # and raises shutil.Error
    # as the file already exists
    
    rem_dirs = walker
    # print(walker[2])
    for data in walker:
        # print(data)
        print(data[2])
        filesN = (len(data[2]))
        print(filesN)
        # testN = filesN // 2
        files = data[2]
        # print(data[2])
        for i in range(filesN):
            try:
               name = files[i].split(".")
               print(name[0][:-5])
            except shutil.Error:
    # to be on the safer side
                print("ERROR!")
                continue

# make_test_data("./lfw", "lfw_test")
view_files("./lfw_test")
# print(5//2)
# resize2("./lfw")
