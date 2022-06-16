from collections import deque

elves = deque([int(n) for n in input().split()])
boxes = [int(n) for n in input().split()]

energy_spent = 0
toys = 0
counter = 0

while boxes and elves:
    current_elf = elves.popleft()
    current_box = boxes.pop()
    if current_elf < 5:
        boxes.append(current_box)
        continue
    else:
        counter += 1
        toys_to_be_created = 1
        energy_to_be_spent = current_box
        energy_increase = 1

        if counter % 3 == 0:
            toys_to_be_created = 2
            energy_to_be_spent *= 2
        if counter % 5 == 0:
            toys_to_be_created = 0
            energy_increase = 0

        if current_elf >= energy_to_be_spent:
            toys += toys_to_be_created
            current_elf = current_elf - energy_to_be_spent + energy_increase  # decrease elf energy
            energy_spent += energy_to_be_spent  # increase energy_spend
        else:
            boxes.append(current_box)
            current_elf *= 2
        elves.append(current_elf)

print(f"Toys: {toys}")
print(f"Energy: {energy_spent}")
if elves:
    print(f"Elves left: {', '.join([str(e) for e in elves])}")
if boxes:
    print(f"Boxes left: {', '.join([str(b) for b in boxes])}")
