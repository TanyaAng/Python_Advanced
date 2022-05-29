def read_square_matrix():
    rows = int(input())
    matrix = []
    for _ in range(rows):
        matrix.append([int(x) for x in input().split()])
    return matrix


def explode_all_cells_around_current(i_coord, j_coord, matrix):
    n = len(matrix)
    m = len(matrix[0])
    current_cell = matrix[i_coord][j_coord]
    start_row = 0
    end_row = i_coord
    start_col = 0
    end_col = j_coord

    if i_coord - 1 in range(0, n):
        start_row = i_coord - 1
    if i_coord + 1 in range(0, n):
        end_row = i_coord + 1
    if j_coord - 1 in range(0, m):
        start_col = j_coord - 1
    if j_coord + 1 in range(0, m):
        end_col = j_coord + 1

    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            if matrix[row][col] > 0:
                matrix[row][col] -= current_cell


def alive_cells(matrix):
    counter = 0
    total_sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > 0:
                counter += 1
                total_sum += matrix[i][j]

    return counter, total_sum

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(' '.join(str(matrix[i][j]) for j in range(len(matrix[0]))))

matrix = read_square_matrix()
bombs_coord = input().split()
bombs = []
for bomb in bombs_coord:
    i, j = [int(x) for x in bomb.split(',')]
    bombs.append((i, j))

for bomb in bombs:
    i, j = bomb[0], bomb[1]
    if matrix[i][j] > 0:
        explode_all_cells_around_current(i, j, matrix)

alive_cells, sum_alive = alive_cells(matrix)
print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_alive}")
print_matrix(matrix)
