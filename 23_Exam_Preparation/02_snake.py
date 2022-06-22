def read_matrix(n):
    matrix = []
    for _ in range(n):
        matrix.append(list(input()))
    return matrix


def find_coord(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'S':
                return (i, j)


def find_burrows(matrix):
    burrows_coords = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'B':
                burrows_coords.append((i, j))
    return burrows_coords

def print_matrix(matrix):
    for row in range(len(matrix)):
        print(''.join(str(matrix[row][col]) for col in range(len(matrix[0]))))


n = int(input())
matrix = read_matrix(n)
row, col = find_coord(matrix)
burrows_coord = find_burrows(matrix)

directions = {'right': lambda r, c: (r, c + 1), 'left': lambda r, c: (r, c - 1),
              'up': lambda r, c: (r - 1, c), 'down': lambda r, c: (r + 1, c)}

food_eated = 0
is_snake_goes_out_of_teritory=False
while True:
    command = input()
    previous_row, previous_col = row, col
    row, col = directions[command](row, col)
    if 0 <= row < n and 0 <= col < n:
        matrix[previous_row][previous_col] = '.'
        if matrix[row][col] == 'B':
            matrix[row][col] = '.'
            for i, j in burrows_coord:
                if (row, col) != (i, j):
                    row, col = i, j
                    matrix[row][col] = 'S'
        elif matrix[row][col] == '*':
            matrix[row][col]='S'
            food_eated += 1
            if food_eated>=10:
                print("You won! You fed the snake.")
                break
            matrix[row][col] = 'S'
        else:
            matrix[row][col] = 'S'

    else:
        matrix[previous_row][previous_col]='.'
        print("Game over!")
        break


print(f"Food eaten: {food_eated}")
print_matrix(matrix)

