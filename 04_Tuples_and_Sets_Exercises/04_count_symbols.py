expression=list(input())
unique_chars={}

for ch in expression:
    if ch not in unique_chars:
        unique_chars[ch]=0
    unique_chars[ch]+=1


for key, value in sorted(unique_chars.items()):
    print(f"{key}: {value} time/s")