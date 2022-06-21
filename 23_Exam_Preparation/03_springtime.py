def start_spring (**kwargs):
    flowers_dict= {}
    for key,value in kwargs.items():
        if value not in flowers_dict:
            flowers_dict[value]=[]
        flowers_dict[value].append(key)

    result=''
    for key,value in sorted(flowers_dict.items(), key=lambda kvp:(-len(kvp[1]),kvp[0])):
        result+=f'{key}:\n'
        for v in sorted(value):
            result+=f'-{v}\n'
    return result



example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
