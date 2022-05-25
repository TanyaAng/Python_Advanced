import math
from collections import deque
expression=input().split()
#stack
numbers=deque([])
VALID_EXPRESSION_SIGNS=['*','+','-','/']

def make_operations_upon_numbers(sign, numbers):
    result = numbers.popleft()
    if sign == '*':
        while numbers:
            result *=numbers.popleft()
        numbers.appendleft(result)
    elif el == '+':
        while numbers:
            result += numbers.popleft()
        numbers.appendleft(result)
    elif el == '-':
        while numbers:
            result -= numbers.popleft()
        numbers.appendleft(result)
    elif el == '/':
        while numbers:
            result /= numbers.popleft()
        numbers.appendleft(math.floor(result))
    return math.floor(result)

for el in expression:
    if el not in VALID_EXPRESSION_SIGNS:
        numbers.append(int(el))
    else:
        result=make_operations_upon_numbers(el,numbers)

print(result)
