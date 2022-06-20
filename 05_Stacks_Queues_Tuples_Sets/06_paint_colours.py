MAIN_COLOURS = {'red', 'yellow', 'blue'}
SECONDARY_COLOURS = {'orange', 'purple', 'green'}
found_colours = []
not_found_colours=[]
data = input().split()
while data:
    current_lenght = len(data)
    middle = current_lenght // 2
    first_item = data.pop(0)
    last_item = ''
    if data:
        last_item = data.pop()
    new_colours = {first_item + last_item, last_item + first_item}

    if MAIN_COLOURS.intersection(new_colours):
        found_colours.append(MAIN_COLOURS.intersection(new_colours).pop())
    elif SECONDARY_COLOURS.intersection(new_colours):
        found_colours.append(SECONDARY_COLOURS.intersection(new_colours).pop())
    else:
        if first_item and last_item:
            if len(first_item)>1:
                first_item = first_item[0:-1]
                data.insert(middle - 1, first_item)
            if len(last_item)>1:
                last_item = last_item[0:-1]
                data.insert(middle-1, last_item)

for current_colour in found_colours:
    if current_colour == 'orange':
        if 'red' not in found_colours or 'yellow' not in found_colours:
            not_found_colours.append(current_colour)
    elif current_colour == 'purple':
        if 'red' not in found_colours or 'blue' not in found_colours:
            not_found_colours.append(current_colour)
    elif current_colour == 'green':
        if 'yellow' not in found_colours or 'blue' not in found_colours:
            not_found_colours.append(current_colour)

for colour in not_found_colours:
    found_colours.remove(colour)

print(found_colours)