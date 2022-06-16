def negative_vs_positive (*args):
    sum_positive=0
    sum_negative=0

    for n in args:
        if n<0:
            sum_negative+=n
        else:
            sum_positive+=n
    result=f"{sum_negative}\n{sum_positive}\n"
    if abs(sum_negative)>abs(sum_positive):
        result+=f"The negatives are stronger than the positives"
    else:
        result+=f"The positives are stronger than the negatives"

    print (result)

numbers=[int(x) for x in input().split()]
negative_vs_positive(*numbers)
