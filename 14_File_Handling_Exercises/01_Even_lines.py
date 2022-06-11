lines_counter=0
signs=['-',',','.','!','?']
with open ('./text.txt', 'r') as file:
    for line in file:
        if lines_counter==0 or lines_counter%2==0:
            text=line.split()
            reversed_text=list(reversed(text))
            new_line=[]
            for word in reversed_text:
                for ch in word:
                    if ch in signs:
                        word=word.replace(ch,'@')
                new_line.append(word)
            print(" ".join(new_line))
        lines_counter+=1
