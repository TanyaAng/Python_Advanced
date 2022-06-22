def check_if_gift_can_be_made (gifts,presents, current_sum):
    for key, value in gifts.items():
        if value[0]<=current_sum<=value[1]:
            if key not in presents:
                presents[key] = 0
            presents[key] += 1

from collections import deque

gifts = {'Gemstone': [100,199], 'Porcelain Sculpture': [200,299], 'Gold': [300,399],
         'Diamond Jewellery': [400,499]}

presents = {}

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    current_sum = current_material + current_magic
    if current_sum < 100:
        if current_sum % 2 == 0:
            current_material *= 2
            current_magic *= 3
            current_sum = current_material + current_magic
        else:
            current_sum *= 2
        check_if_gift_can_be_made(gifts,presents,current_sum)

    elif current_sum > 499:
        current_sum /= 2
        check_if_gift_can_be_made(gifts,presents,current_sum)

    else:
        check_if_gift_can_be_made(gifts,presents,current_sum)


if 'Gemstone' in presents and 'Porcelain Sculpture' in presents:
    print('The wedding presents are made!')
elif 'Gold' in presents and 'Diamond Jewellery' in presents:
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

for key, value in sorted(presents.items()):
    print(f'{key}: {value}')
