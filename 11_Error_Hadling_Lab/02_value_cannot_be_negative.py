class ValueCannotBeNegative(Exception):
    pass

values=[int(input()) for _ in range(5)]

for value in values:
    if value < 10:
        raise ValueCannotBeNegative(f"{value} cannot be negative.")
