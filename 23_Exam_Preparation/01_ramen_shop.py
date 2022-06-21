from collections import deque

ramen=[int(x) for x in input().split(', ')]
customers=deque([int(x) for x in input().split(', ')])


while ramen and customers:
    current_ramen=ramen.pop()
    current_customer=customers.popleft()
    if current_ramen>current_customer:
        current_ramen-=current_customer
        ramen.append(current_ramen)
    elif current_ramen<current_customer:
        current_customer-=current_ramen
        customers.appendleft(current_customer)

if not customers:
    print(f"Great job! You served all the customers.")
    if ramen:
        print(f"Bowls of ramen left: {', '.join([str(x) for x in ramen])}")
if customers and not ramen:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f"Customers left: {', '.join([str(x) for x in customers])}")

