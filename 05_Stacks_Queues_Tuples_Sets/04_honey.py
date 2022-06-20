from collections import deque

def calculate_honey_made(bee,nectar,symbol):
    if symbol=="+":
        return abs(bee+nectar)
    elif symbol=='-':
        return abs (bee-nectar)
    elif symbol=='*':
        return abs(bee*nectar)
    elif symbol=='/':
        if nectar!=0:
            return abs(bee/nectar)
        return 0

bees=deque([int(x) for x in input().split()])
nectars=[int(x) for x in input().split()]
operations=deque(input().split())

honey_made=0

while bees and nectars:
    bee=bees.popleft()
    nectar=nectars.pop()
    if nectar<bee:
        bees.appendleft(bee)
        continue
    else:
        symbol=operations.popleft()
        honey_made+=calculate_honey_made(bee,nectar,symbol)

print(f"Total honey made: {honey_made}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectars:
    print(f"Nectars left: {', '.join([str(x) for x in nectars])}")











































