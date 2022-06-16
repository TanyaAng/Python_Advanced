def even_odd (*args):
    command=args[-1]
    numbers=args[0:-1]
    result=[]

    if command=='even':
        result=[n for n in numbers if n%2==0]
    elif command=='odd':
        result = [n for n in numbers if n % 2 != 0]
    return result




print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))