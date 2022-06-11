signs=["-",",",".","!","?","'"]
lines_counter=1
file_to_write=open('./output.txt','a')
with open('./text.txt', 'r') as file:
    for line in file:
        text=line
        chars_counter=0
        sign_counter=0
        for ch in text:
            if ch.isalpha():
                chars_counter+=1
            elif ch in signs:
                sign_counter+=1
        file_to_write.writelines(f"Line {lines_counter}: {text} ({chars_counter})({sign_counter})\n")
        lines_counter+=1

