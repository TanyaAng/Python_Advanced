def raise_exception_value_must_be_integer():
    return f"The variable number must be an integer"

def raise_exception_number_does_not_exist():
    return f"Number does not exist in dictionary"

numbers_dictionary = {}

while True:
    line = input()
    if line == "Search":
        break
    try:
        number_as_string = line
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print(raise_exception_value_must_be_integer())

while True:
    line = input()
    if line == "Remove":
        break
    searched = line
    try:
        print(numbers_dictionary[searched])
    except ValueError:
        print(raise_exception_number_does_not_exist())

while True:
    line = input()
    if line == "End":
        break
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print(raise_exception_number_does_not_exist())

print(numbers_dictionary)
