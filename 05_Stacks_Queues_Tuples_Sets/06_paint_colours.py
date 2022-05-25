from collections import deque

substrings = deque(input().split())
collected_colours = []
collected_secondary_colours = []

MAIN_COLORS = ['red', 'yellow', 'blue']
SECONDARY_COLORS = ['orange', 'purple', 'green']

while substrings:
    first_substring = substrings.popleft()
    last_substring = ''
    s_lenght = len(last_substring)
    f_lenght = len(first_substring)
    new_colour = first_substring
    if substrings:
        last_substring = substrings.pop()
        s_lenght = len(last_substring)
        left_concat = first_substring + last_substring
        right_concat = last_substring + first_substring
        if left_concat in MAIN_COLORS or left_concat in SECONDARY_COLORS:
            new_colour = left_concat
        elif right_concat in MAIN_COLORS or right_concat in SECONDARY_COLORS:
            new_colour = right_concat

    if new_colour in MAIN_COLORS or new_colour in SECONDARY_COLORS:
        collected_colours.append(new_colour)
    else:
        first_substring = first_substring[0:f_lenght - 1]
        if last_substring:
            last_substring = last_substring[0:s_lenght - 1]
        middle_of_expression = len(substrings) // 2
        if len(substrings) % 2 != 0:
            middle_of_expression -= 1
        if first_substring != '' and last_substring != '':
            substrings.insert(middle_of_expression, first_substring)
            substrings.insert(middle_of_expression + 1, last_substring)
        elif first_substring != '' and last_substring == '':
            substrings.insert(middle_of_expression, first_substring)
        elif first_substring == '' and last_substring != '':
            substrings.insert(middle_of_expression, last_substring)

for colour in collected_colours:
    if colour == 'orange':
        if 'red' not in collected_colours or 'yellow' not in collected_colours:
            collected_colours.remove(colour)
    elif colour == 'purple':
        if 'red' not in collected_colours or 'blue' not in collected_colours:
            collected_colours.remove(colour)
    elif colour == 'green':
        if 'yellow' not in collected_colours or 'blue' not in collected_colours:
            collected_colours.remove(colour)

print(collected_colours)
