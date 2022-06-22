from math import log, e

value=int(input())
base=input()
if base.isdigit():
    print(f"{log(value,int(base)):.2f}")
elif base=='natural':
    print(f"{log(value, e):.2f}")

