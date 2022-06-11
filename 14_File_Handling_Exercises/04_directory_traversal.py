import os
list_of_files_in_dir=[]

current_dir=os.walk(input())
for root, dirs, files in current_dir:
    list_of_files_in_dir.append(files)

dict_of_files={}
for list in list_of_files_in_dir:
    for file in list:
        file_type='.'+file.split(".")[1]
        if file_type not in dict_of_files:
            dict_of_files[file_type]=[]
        dict_of_files[file_type].append(file)

result=''
for key, value in sorted(dict_of_files.items(), key=lambda kvp: (kvp[0],kvp[1])):
    result+=key+'\n'
    for v in value:
        result+=f"- - - {v}\n"

print(result)

with open("./report.txt", "w") as file:
    file.write(result)