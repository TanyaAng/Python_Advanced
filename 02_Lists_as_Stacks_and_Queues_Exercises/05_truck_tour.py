petrol_stations=int(input())

track_consumption=1
petrols_in_tank=0

for _ in range (petrol_stations):
    p, d=input().split()
    amount_petrol=int(p)
    distance=int(d)
