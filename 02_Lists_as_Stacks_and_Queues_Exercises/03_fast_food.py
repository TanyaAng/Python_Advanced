def find_biggest_order(queue):
    if queue:
        print (max(queue))

from collections import deque
food_per_day=int(input())
food_orders=deque(map(int, input().split()))
find_biggest_order(food_orders)

while food_orders:
    current_order=food_orders.popleft()
    if current_order<=food_per_day:
        food_per_day-=current_order
    else:
        food_orders.appendleft(current_order)
        break

if food_orders:
    print(f"Orders left: {' '.join(str(el) for el in food_orders)}")
else:
    print("Orders complete")



