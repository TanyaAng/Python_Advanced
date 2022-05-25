from collections import deque
materials=[int(x) for x in input().split()]
magic_values=deque([int(x) for x in input().split()])

total_magic=0
toys={'Doll':150, 'Wooden train':250, 'Teddy bear':300, 'Bicycle':400}
crafted_toys= {}

while True:
    if not materials:
        break
    if not magic_values:
        break

    current_material=materials.pop()
    current_magic=magic_values.popleft()
    magic=current_material*current_magic

    if current_material==0 or current_magic==0:
        if current_material!=0:
            materials.append(current_material)
        if current_magic!=0:
            magic_values.appendleft(current_magic)
        continue
    if magic in toys.values():
        for key,value in toys.items():
            if magic==value:
                toy=key
                if toy not in crafted_toys:
                    crafted_toys[toy]=0
                crafted_toys[toy]+=1
    elif magic<0:
        magic=current_magic+current_material
        materials.append(magic)
    elif magic>0:
        current_material+=15
        materials.append(current_material)

is_presents_crafted=False

if 'Doll' in crafted_toys.keys() and 'Train' in crafted_toys.keys():
    is_presents_crafted=True
elif 'Teddy bear' in crafted_toys.keys() and 'Bicycle' in crafted_toys.keys():
    is_presents_crafted=True

if is_presents_crafted:
    print("The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")
if magic_values:
    print(f"Magic left: {', '.join([str(x) for x in magic_values])}")

for key,value in sorted(crafted_toys.items()):
    print(f"{key}: {value}")









