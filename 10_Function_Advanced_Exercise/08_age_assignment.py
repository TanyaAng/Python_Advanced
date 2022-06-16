def age_assignment(*args, **kwargs):
    name_age_register={}
    result=''
    for name in args:
        if name not in name_age_register:
            name_age_register[name]=0
    for key, value in kwargs.items():
        for name in name_age_register.keys():
            if key==name[0]:
                name_age_register[name]=value
    for key,value in sorted(name_age_register.items(), key=lambda kvp: kvp[0]):
        result+=f"{key} is {value} years old.\n"
    return result

print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))


