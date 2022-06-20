def read_matrix(size):
    matrix = []
    for _ in range(size):
        matrix.append([x for x in input().split()])
    return matrix


def find_current_place(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 'A':
                return (i, j)


def calculate_targers(matrix):
    targets = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 'x':
                targets += 1
    return targets


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))


SIZE = 5
directions = {'right': lambda r, c, step: (r, c + step), 'left': lambda r, c, step: (r, c - step),
              'up': lambda r, c, step: (r - step, c), 'down': lambda r, c, step: (r + step, c)}
matrix = read_matrix(SIZE)
row, col = find_current_place(matrix)
shot_targets = 0
targets = calculate_targers(matrix)
targets_path = []
for _ in range(int(input())):
    data = input()
    if data.startswith('move'):
        command, direction, steps = data.split()
        steps = int(steps)
        next_row, next_col = directions[direction](row, col, steps)
        if next_row in range(SIZE) and next_col in range(SIZE) and matrix[next_row][next_col] == '.':
            matrix[row][col] = '.'
            row, col = next_row, next_col
            matrix[row][col] = 'A'
    elif data.startswith('shoot'):
        command, direction = data.split()
        row_to_shoot, col_to_shoot = directions[direction](row, col, 1)
        while row_to_shoot in range(SIZE) and col_to_shoot in range(SIZE):
            if matrix[row_to_shoot][col_to_shoot] == 'x':
                matrix[row_to_shoot][col_to_shoot] = '.'
                shot_targets += 1
                targets_path.append([row_to_shoot, col_to_shoot])
                break
            row_to_shoot, col_to_shoot = directions[direction](row_to_shoot, col_to_shoot, 1)
    left_targets = calculate_targers(matrix)
    if left_targets == 0:
        break

if shot_targets == targets:
    print(f"Training completed! All {targets} targets hit.")
else:
    print(f"Training not completed! {abs(targets - shot_targets)} targets left.")

print(*targets_path, sep='\n')
