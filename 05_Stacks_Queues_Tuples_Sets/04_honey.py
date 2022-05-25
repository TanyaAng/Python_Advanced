from collections import deque
working_bees=deque([int(x) for x in input().split()])
nectar=[int(x) for x in input().split()]
honey_process=deque(input().split())

honey_collected=0

def collect_honey(bee,nectar,sign):
    if sign=='+':
        return abs(bee+nectar)
    elif sign=='-':
        return abs(bee-nectar)
    elif sign=='*':
        return abs(bee*nectar)
    elif sign=='/':
        return abs(bee/nectar)

while True:
    if not working_bees:
        break
    if not nectar:
        break
    current_bee=working_bees.popleft()
    current_nectar=nectar.pop()
    if current_nectar>=current_bee:
        sign=honey_process.popleft()
        honey_collected+=collect_honey(current_bee,current_nectar,sign)
    else:
        working_bees.appendleft(current_bee)


print(f"Total honey made: {honey_collected}")
if working_bees:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")





