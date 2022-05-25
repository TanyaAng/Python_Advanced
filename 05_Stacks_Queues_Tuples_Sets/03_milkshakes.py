from collections import deque
chocolate=list(map(int,input().split(',')))
milk_cups=deque(list(map(int,input().split(','))))
milkshakes_counter=0
while True:
    if not chocolate:
        break
    if not milk_cups:
        break
    current_chocolate=chocolate.pop()
    current_milk = milk_cups.popleft()

    if current_chocolate<=0 or current_milk<=0:
        if current_chocolate>0:
            chocolate.append(current_chocolate)
        elif current_milk>0:
            milk_cups.appendleft(current_milk)
        continue
    if current_milk==current_chocolate:
        milkshakes_counter+=1
        if milkshakes_counter>=5:
            break
    else:
        milk_cups.append(current_milk)
        current_chocolate-=5
        chocolate.append(current_chocolate)

if milkshakes_counter>=5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')
if chocolate:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")
else:
    print("Chocolate: empty")
if milk_cups:
    print(f"Milk: {', '.join([str(x) for x in milk_cups])}")
else:
    print("Milk: empty")

