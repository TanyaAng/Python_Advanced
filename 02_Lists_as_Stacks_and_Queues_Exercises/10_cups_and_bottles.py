from collections import deque
cups=deque(list(map(int,input().split())))
bottles=list(map(int,input().split()))

wasted_water=0
while cups:
    if bottles:
        current_cup = cups.popleft()
        current_bottle=bottles.pop()
        if current_bottle<current_cup:
            current_cup-=current_bottle
            cups.appendleft(current_cup)
            continue
        else:
            wasted_water+=current_bottle-current_cup
    else:
        break

if not cups and bottles:
    print(f"Bottles: {' '.join([str(b) for b in bottles])}")
if not bottles and cups:
    print(f"Cups: {' '.join([str(c) for c in cups])}")
print(f"Wasted litters of water: {wasted_water}")



