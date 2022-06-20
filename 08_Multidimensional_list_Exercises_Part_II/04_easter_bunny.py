import sys


def read_square_matrix(size):
    matrix = []
    for _ in range(size):
        matrix.append(input().split())
    return matrix


def find_bunny_coordinates(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'B':
                return (i, j)


def find_max_path(bunny_coords, matrix):
    bunny_row, bunny_col = bunny_coords
    directions = {'up': lambda r, c: (r - 1, c), 'down': lambda r, c: (r + 1, c), 'left': lambda r, c: (r, c - 1),
                  'right': lambda r, c: (r, c + 1)}
    best_sum = -sys.maxsize
    best_dir = ''
    best_path = []
    for dir in directions:
        row, col = directions[dir](bunny_row, bunny_col)
        current_sum = 0
        current_path = []
        while 0 <= row < len(matrix) and 0 <= col < len(matrix) and matrix[row][col] != 'X':
            current_sum += int(matrix[row][col])
            if int(matrix[row][col])>=0:
                current_path.append([row, col])
            if current_sum > best_sum and current_path:
                best_sum = current_sum
                best_path = current_path
                best_dir = dir
            row, col = directions[dir](row, col)
    return best_dir, best_path, best_sum


size = int(input())
matrix = read_square_matrix(size)
bunny_coods = find_bunny_coordinates(matrix)
direction, path, total_eggs = find_max_path(bunny_coods, matrix)
print(direction)
print(*path, sep='\n')
print(total_eggs)
