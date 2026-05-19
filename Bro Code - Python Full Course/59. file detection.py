# Python file detection

import os

file_path = "stuff/test.txt"
file_path_direct_v1 = "C:\\Users\\laczk\\Desktop\\test.txt"
file_path_direct_v2 = "C:/Users/laczk/Desktop/test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path} exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location doesn't exist")