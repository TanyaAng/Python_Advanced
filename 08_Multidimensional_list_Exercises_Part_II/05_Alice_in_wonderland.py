def read_square_matrix(size):
    matrix = []
    for _ in range(size):
        matrix.append(input().split())
    return matrix


def find_Alice_coordinates(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'A':
                return (i, j)


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))


matrix = read_square_matrix(int(input()))
Alice_coords = find_Alice_coordinates(matrix)
total_tea_bags = 0
is_Alice_went_to_party = True
row, col = Alice_coords
matrix[row][col] = '*'
directions = {'up': lambda r, c: (r - 1, c), 'down': lambda r, c: (r + 1, c), 'left': lambda r, c: (r, c - 1),
              'right': lambda r, c: (r, c + 1)}
while True:
    command = input()
    row, col = directions[command](row, col)
    if row not in range(0, len(matrix)) or col not in range(0, len(matrix)):
        is_Alice_went_to_party = False
        break
    else:
        if matrix[row][col] == 'R':
            matrix[row][col] = '*'
            is_Alice_went_to_party = False
            break
        elif matrix[row][col] in ['*','.']:
            matrix[row][col] = '*'
        else:
            total_tea_bags += int(matrix[row][col])
            matrix[row][col]='*'
            if total_tea_bags >= 10:
                break

if is_Alice_went_to_party:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

print_matrix(matrix)
