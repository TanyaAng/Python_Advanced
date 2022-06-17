def found_is_unique_by_number(kids, number):
    is_unique = False
    found_kid = None
    for n, kid_name in kids:
        if number == n and is_unique:
            return False, None
        if number == n:
            is_unique = True
            found_kid = kid_name
    if is_unique:
        return True, found_kid
    else:
        return False, None


def found_is_unique_by_name(kids, name):
    is_unique = False
    number = None
    found_kid = None
    for n, kid_name in kids:
        if name == kid_name and is_unique:
            return False, None, None
        if name == kid_name:
            is_unique = True
            found_kid = kid_name
            number = n
    if is_unique:
        return True, number, found_kid
    else:
        return False, None, None


def naughty_or_nice_list(kids, *args, **kwargs):
    kids_dict = {'Nice': [], 'Naughty': [], 'Not found': []}
    for command in args:
        number, type = command.split('-')
        number = int(number)
        is_unique, found_kid = found_is_unique_by_number(kids, number)
        if is_unique:
            kids.remove((number, found_kid))
            kids_dict[type].append(found_kid)

    if kwargs:
        for name, type in kwargs.items():
            is_unique, found_number, found_kid = found_is_unique_by_name(kids, name)
            if is_unique:
                kids.remove((found_number, found_kid))
                kids_dict[type].append(found_kid)

    if kids:
        for kid in kids:
            kids_dict['Not found'].append(kid[1])

    result = ''
    for type, kids in kids_dict.items():
        if kids:
            result += f"{type}: {', '.join(kids)}\n"
    return result


# print(naughty_or_nice_list(
#     [
#         (3, "Amy"),
#         (1, "Tom"),
#         (7, "George"),
#         (3, "Katy"),
#     ],
#     "3-Nice",
#     "1-Naughty",
#     Amy="Nice",
#     Katy="Naughty",
# ))
#
# print(naughty_or_nice_list(
#     [
#         (7, "Peter"),
#         (1, "Lilly"),
#         (2, "Peter"),
#         (12, "Peter"),
#         (3, "Simon"),
#     ],
#     "3-Nice",
#     "5-Naughty",
#     "2-Nice",
#     "1-Nice",
# ))
#
# print(naughty_or_nice_list(
#     [
#         (6, "John"),
#         (4, "Karen"),
#         (2 , "Tim"),
#         (1, "Merry"),
#         (6, "Frank"),
#     ],
#     "6-Nice",
#     "5-Naughty",
#     "4-Nice",
#     "3-Naughty",
#     "2-Nice",
#     "1-Naughty",
#     Frank="Nice",
#     Merry="Nice",
#     John="Naughty",
# ))
