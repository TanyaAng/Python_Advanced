def read_matrix(n, m):
    matrix = []
    for _ in range(n):
        matrix.append(list(input()))
    return matrix


def find_player_coord(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'P':
                return (i, j)


def print_matrix(matrix):
    [print(''.join(row)) for row in matrix]


def spread_bunnies(matrix):
    bunnies_coords = []
    is_player_dies = False
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'B':
                bunnies_coords.append((i, j))
    for i, j in bunnies_coords:
        for dir in directions:
            current_i, current_j = directions[dir](i, j)
            if current_i in range(len(matrix)) and current_j in range(len(matrix[0])):
                if matrix[current_i][current_j] == 'P':
                    matrix[current_i][current_j] = 'B'
                    is_player_dies = True
                else:
                    matrix[current_i][current_j] = 'B'
    return is_player_dies, matrix


n, m = [int(x) for x in input().split()]
matrix = read_matrix(n, m)

row, col = find_player_coord(matrix)

commands = list(input())

directions = {'U': lambda r, c: (r - 1, c), 'D': lambda r, c: (r + 1, c), 'L': lambda r, c: (r, c - 1),
              'R': lambda r, c: (r, c + 1)}

is_player_dies = False
is_player_win = False
for dir in commands:
    previous_row=row
    previous_col=col
    row, col = directions[dir](row, col)
    if row in range(len(matrix)) and col in range(len(matrix[0])):
        if matrix[row][col] == 'B':
            is_player_dies, matrix = spread_bunnies(matrix)
            # print('------------')
            print_matrix(matrix)
            print(f'dead: {row} {col}')
            break
        else:
            matrix[previous_row][previous_col]='.'
            matrix[row][col] = 'P'
            is_player_dies, matrix = spread_bunnies(matrix)
            # print('---Step---')
            # print_matrix(matrix)
            if is_player_dies:
                # print('------------')
                print_matrix(matrix)
                print(f'dead: {row} {col}')
                break
    else:
        matrix[previous_row][previous_col]='.'
        is_player_win = True
        is_player_dies,matrix=spread_bunnies(matrix)
        # print('------------')
        print_matrix(matrix)
        print(f'won: {previous_row} {previous_col}')
        break
