def is_vip(guest):
    return guest[0].isdigit()

number=int(input())
regular=set()
VIP=set()

for _ in range(number):
    guest=input()
    if is_vip(guest):
        VIP.add(guest)
    else:
        regular.add(guest)

comming_guest=input()
while comming_guest!='END':
    if is_vip(comming_guest):
        VIP.remove(comming_guest)
    else:
        regular.remove(comming_guest)
    comming_guest=input()

missing_guests=len(regular)+len(VIP)
print(missing_guests)
[print(guest) for guest in sorted(VIP)]
[print(guest) for guest in sorted(regular)]

