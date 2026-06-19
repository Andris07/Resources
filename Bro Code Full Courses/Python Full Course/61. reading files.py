# Python reading files (.txt, .json, .csv)

import json
import csv

file_path = "./stuff/output.txt" # .json, .csv

try:
    with open(file_path, "r") as file:
        content = file.read()
        # content = json.load(file)   -> .json file extension
        # content = csv.reader(file)  -> .csv  file extension
        print(content)
        # print(content["name"])      -> .json file extension
        # for line in content:        -> .csv  file extension
        #     print(line[0])             
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")