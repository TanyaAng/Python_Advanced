number=int(input())
cars_register=set()
for _ in range (number):
    direction, car=input().split(", ")
    if direction=='IN':
        cars_register.add(car)
    elif direction=='OUT':
        if car in cars_register:
            cars_register.remove(car)

if not cars_register:
    print(f"Parking Lot is Empty")
else:
    print('\n'.join(cars_register))

