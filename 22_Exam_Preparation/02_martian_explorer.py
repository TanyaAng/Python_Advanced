def read_square_matrix(size=6):
    matrix = []
    for _ in range(size):
        matrix.append([x for x in input().split()])
    return matrix


def print_matrix(matrix):
    for row in range(len(matrix)):
        print(' '.join(str(matrix[row][col]) for col in range(len(matrix[0]))))


def find_rover_position(matrix, rover='E'):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == rover:
                position = (row, col)
                return position


def find_next_step(matrix_size, command, row, col):
    if command == 'up':
        if row - 1 in range(matrix_size):
            row -= 1
        else:
            row = len(matrix) - 1
    elif command == 'down':
        if row + 1 in range(matrix_size):
            row += 1
        else:
            row = 0
    elif command == 'left':
        if col - 1 in range(matrix_size):
            col -= 1
        else:
            col = len(matrix) - 1
    elif command == 'right':
        if col + 1 in range(matrix_size):
            col += 1
        else:
            col = 0
    return row, col


matrix = read_square_matrix()
rover_position = find_rover_position(matrix)
water_deposit = 0
metal_deposit = 0
concrete_deposit = 0
commands = input().split(", ")
row, col = rover_position
is_broken = False
for command in commands:
    row, col = find_next_step(len(matrix), command, row, col)
    if matrix[row][col] == 'R':
        print(f'Rover got broken at {row, col}')
        is_broken = True
        break
    elif matrix[row][col] == 'W':
        water_deposit += 1
        print(f"Water deposit found at {row, col}")
    elif matrix[row][col] == 'M':
        metal_deposit += 1
        print(f"Metal deposit found at {row, col}")
    elif matrix[row][col] == 'C':
        concrete_deposit += 1
        print(f"Concrete deposit found at {row, col}")

if water_deposit >= 1 and metal_deposit >= 1 and concrete_deposit >= 1:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
