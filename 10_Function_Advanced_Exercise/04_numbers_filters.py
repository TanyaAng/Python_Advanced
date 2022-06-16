def even_odd_filter(**kwargs):
    dict_numbers=kwargs
    for key, value in dict_numbers.items():
        if key=='odd':
            dict_numbers[key]=[v for v in value if v%2!=0]
        elif key=='even':
            dict_numbers[key]=[v for v in value if v%2==0]
    return dict(sorted(dict_numbers.items(), key=lambda kvp:len(kvp[1]), reverse=True))

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
