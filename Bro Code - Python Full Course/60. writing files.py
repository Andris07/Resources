# Python writing files (.txt, .json, .csv)

import json
import csv

txt_data = "I like pizza!"

file_path = "stuff/output.txt"
file_path_direct_v1 = "C:\\Users\\laczk\\Desktop\\output.txt"
file_path_direct_v2 = "C:/Users/laczk/Desktop/output.txt"

try:
    with open(file_path, "x") as file:
        file.write(txt_data)
        print(f"txt file '{file_path}' was created with create mode")
except FileExistsError:
    print("That file already exists")

with open(file_path, "w") as file:
        file.write(txt_data)
        print(f"txt file '{file_path}' was created (or overwritten) with write mode")

txt_data = "I like hamburger also!"

with open(file_path, "a") as file:
        file.write("\n" + txt_data)
        print(f"txt file '{file_path}' was modified with append mode")

employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

with open(file_path, "w") as file:
        for employee in employees:
            file.write(employee + "\n")
        print(f"txt file '{file_path}' was created (or overwritten) with write mode")

file_path_json = "stuff/output.json"

employee =  {
                "name": "Spongebob",
                "age": 30,
                "job": "cook",
            }

try:
    with open(file_path_json, "w") as file:
        json.dump(employee, file, indent=4)
        print(f"json file '{file_path_json}' was created (or overwritten) with write mode")
except FileExistsError:
    print("That file already exists")

employees = [
                ["Name", "Age", "Job"],
                ["Spongebob", 30, "cook"],
                ["Patrick", 37, "Unemployed"],
                ["Sandy", 27, "Scientist"],
            ]

file_path_csv = "stuff/output.csv"

try:
    with open(file_path_csv, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path_csv}' was created (or overwritten) with write mode")
except FileExistsError:
    print("That file already exists")
