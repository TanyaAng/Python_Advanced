def naughty_or_nice_list (*args,**kwargs):
    kids_dict={'Nice':[],'Naughty':[], 'Not found':[]}
    list_of_kids=args[0]
    for i in range(1,len(args)):
        number,type=args[i].split('-')
        number=int(number)
        kids_out_of_list = []
        for kid in list_of_kids:
            n,kid_name=kid
            if number==n:
                kids_dict[type].append(kid_name)
                kids_out_of_list.append(kid)
                break
        if kids_out_of_list:
            for kid in kids_out_of_list:
                list_of_kids.remove(kid)

    if kwargs:
        for name,type in kwargs.items():
            kids_out_of_list=[]
            for kid in list_of_kids:
                n,kid_name=kid
                if name==kid_name:
                    kids_dict[type].append(kid_name)
                    kids_out_of_list.append(kid)
                    break
            if kids_out_of_list:
                for kid in kids_out_of_list:
                    list_of_kids.remove(kid)
    if list_of_kids:
        for kid in list_of_kids:
            kids_dict['Not found'].append(kid[1])

    result=''
    for type,kids in kids_dict.items():
        if kids:
            result+=f"{type}: {', '.join(kids)}\n"

    return result


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))


print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))


