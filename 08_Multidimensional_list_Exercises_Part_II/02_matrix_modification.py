def read_square_matrix():
    rows=int(input())
    matrix=[]
    for _ in range(rows):
        matrix.append([int(x) for x in input().split()])
    return matrix

def is_valid_coord (i,j,matrix):
    if i not in range(0,len(matrix)) or j not in range(0, len(matrix[0])):
        return False
    return True

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(' '.join(str(matrix[i][j]) for j in range(len(matrix[0]))))

matrix=read_square_matrix()
while True:
    command=input()
    if command=='END':
        break
    row, col, value = command.split()[1::]
    row = int(row)
    col = int(col)
    value = int(value)
    if not is_valid_coord(row, col, matrix):
        print('Invalid coordinates')
    else:
        if command.startswith('Add'):
            matrix[row][col]+=value
        elif command.startswith('Subtract'):
            matrix[row][col] -= value
print_matrix(matrix)
