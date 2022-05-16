from collections import deque

children = deque(input().split())
n_toss=int(input())

counter=0
while len(children)>1:
    counter+=1
    child=children.popleft()
    if counter%n_toss!=0:
        children.append(child)
    else:
        print(f"Removed {child}")

print(f"Last is {children.pop()}")