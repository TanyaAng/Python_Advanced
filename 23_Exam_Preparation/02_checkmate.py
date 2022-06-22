def read_matrix(size):
    matrix = []
    for _ in range(size):
        matrix.append(input().split())
    return matrix


def check_if_queen_can_capture_king(row, col, matrix, directions):
    queen_row,queen_col=row,col
    for dir in directions:
        row,col=directions[dir](queen_row,queen_col)
        while 0<=row<SIZE and 0<=col<SIZE:
            if matrix[row][col]=='Q':
                break
            if matrix[row][col]=='K':
                return True
            row, col = directions[dir](row, col)
    return False

directions = {'up': lambda r, c: (r - 1, c), 'down': lambda r, c: (r + 1, c), 'left': lambda r, c: (r, c - 1),
              'right': lambda r, c: (r, c + 1), 'diagonal up left': lambda r, c: (r - 1, c - 1),
              'diagonal up right': lambda r, c: (r - 1, c + 1), 'diagonal down left': lambda r, c: (r + 1, c - 1),
              'diagonal down right': lambda r, c: (r + 1, c + 1)}
SIZE = 8
matrix = read_matrix(SIZE)
queens_coords = []

for i in range(SIZE):
    for j in range(SIZE):
        if matrix[i][j] == 'Q':
            if check_if_queen_can_capture_king(i,j,matrix,directions):
                queens_coords.append([i,j])

if queens_coords:
    print(*queens_coords,sep='\n')
else:
    print("The king is safe!")
