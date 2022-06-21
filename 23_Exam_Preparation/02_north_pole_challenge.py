def read_matricx(n, m):
    matrix = []
    for _ in range(n):
        matrix.append(input().split())
    return matrix


def find_your_position(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'Y':
                return (i, j)


def is_left_any_gift(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] in ['D', 'G', 'C']:
                return True
    return False


def print_matrix(matrix):
    [print(' '.join(row)) for row in matrix]


n, m = [int(x) for x in input().split(', ')]
matrix = read_matricx(n, m)
row, col = find_your_position(matrix)

count_decorations = 0
count_gifts = 0
count_cookies = 0

directions = {'right': lambda r, c: (r, c + 1), 'left': lambda r, c: (r, c - 1),
              'up': lambda r, c: (r - 1, c), 'down': lambda r, c: (r + 1, c)}

opposite_side = {'right': lambda r, c: (r, 0), 'left': lambda r, c: (r, len(matrix[0]) - 1),
                 'up': lambda r, c: (len(matrix) - 1, c), 'down': lambda r, c: (0, c)}

while True:
    command = input()
    if command == 'End':
        break
    direction, steps = command.split('-')
    steps = int(steps)
    for step in range(steps):
        previous_row, previous_col = row, col
        row, col = directions[direction](row, col)
        if row not in range(len(matrix)) or col not in range(len(matrix[0])):
            row, col = opposite_side[direction](row, col)
        if matrix[row][col] == 'D':
            count_decorations += 1
        elif matrix[row][col] == 'G':
            count_gifts += 1
        elif matrix[row][col] == 'C':
            count_cookies += 1
        matrix[row][col] = 'Y'
        matrix[previous_row][previous_col] = 'x'

        if not is_left_any_gift(matrix):
            print('Merry Christmas!')
            break
    if not is_left_any_gift(matrix):
        break

print(f"You've collected:\n- {count_decorations} Christmas decorations\n- {count_gifts} Gifts\n- {count_cookies} Cookies")
print_matrix(matrix)
