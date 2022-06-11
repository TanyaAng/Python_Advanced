import os
while True:
    command=input()
    if command=='End':
        break

    elif command.startswith("Create"):
        action,file_name=command.split("-")
        file=open(file_name,'w')

    elif command.startswith("Add"):
        action,file_name,content=command.split("-")
        with open(file_name,'a') as file:
            file.write(f"{content}\n")

    elif command.startswith("Replace"):
        action,file_name,old_string,new_string=command.split("-")
        try:
            with open (file_name, 'r') as file:
                text=file.read()
            new_text = text.replace(old_string, new_string)
            print(new_text)
            file = open(file_name, 'w')
            file.write(new_text)
            file.close()
        except FileNotFoundError:
            print("An error occured")

    elif command.startswith("Delete"):
        action,file_name=command.split("-")
        try:
            os.path.exists(file_name)
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")

