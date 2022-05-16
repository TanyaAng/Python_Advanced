from collections import deque
liters=int(input())
people=deque()

command = input()
while command!='Start':
    people.append(command)
    command = input()

command = input()
while command!='End':
    if command.startswith('refill'):
        params=command.split()
        water_wanted=int(params[1])
        liters+=water_wanted
    else:
        person=people.popleft()
        water_wanted=int(command)
        if water_wanted<=liters:
            print(f"{person} got water")
            liters-=water_wanted
        else:
            print(f"{person} must wait")
    command = input()

print(f"{liters} liters left")