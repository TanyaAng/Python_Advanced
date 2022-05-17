from collections import deque

number_stations=int(input())
petrol_stations=deque([])
petrols_in_tank=0

for _ in range (number_stations):
    petrol_stations.append(input())

for big_station in range (number_stations):
    is_valid = True
    for small_station in range (number_stations):
        current_amount,kilometers=petrol_stations[small_station].split()
        current_amount=int(current_amount)
        kilometers=int(kilometers)
        petrols_in_tank += current_amount
        if petrols_in_tank>=kilometers:
            petrols_in_tank-=kilometers
        else:
            petrols_in_tank=0
            is_valid=False
            break
    if is_valid:
        print (big_station)
        break
    else:
        petrol_stations.rotate(-1)

