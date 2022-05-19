data=tuple(map(float, input().split()))
dict_data={}

for el in data:
    if el not in dict_data:
        dict_data[el]=0
    dict_data[el]+=1

for key, value in dict_data.items():
    print(f"{key:.1f} - {value} times")