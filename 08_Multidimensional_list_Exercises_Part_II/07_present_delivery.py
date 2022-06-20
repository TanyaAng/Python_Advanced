def read_matrix(size):
    matrix = []
    for _ in range(size):
        matrix.append([x for x in input().split()])
    return matrix


def print_matrix(matrix):
    [print(' '.join(row)) for row in matrix]


def find_Santas_coord(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 'S':
                return (i, j)


def calculate_nice_kid(matrix):
    nice_kids = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 'V':
                nice_kids += 1
    return nice_kids

Santa_presents = int(input())
neighborhood = int(input())
matrix = read_matrix(neighborhood)
row, col = find_Santas_coord(matrix)
nice_kids=calculate_nice_kid(matrix)
gift_to_nice_kids=0
is_ran_out_of_presents=False
directions = {'left': lambda r, c: (r, c - 1),
              'right': lambda r, c: (r, c + 1),'up': lambda r, c: (r - 1, c), 'down': lambda r, c: (r + 1, c) }
while True:
    command = input()
    if command == 'Christmas morning':
        break
    matrix[row][col] = '-'
    row, col = directions[command](row, col)
    if row in range(len(matrix)) and col in range(len(matrix)):
        if matrix[row][col] == 'V':
            matrix[row][col] = 'S'
            gift_to_nice_kids+=1
            Santa_presents-=1
            if Santa_presents == 0:
                is_ran_out_of_presents=True
                break
        elif matrix[row][col] == 'C':
            cookie_cell = (row, col)
            matrix[row][col] = 'S'
            for dir in directions:
                r, c = directions[dir](row, col)
                if r in range(len(matrix)) and c in range (len(matrix)) and matrix[r][c] in ['X', 'V']:
                    if matrix[r][c]=='V':
                        gift_to_nice_kids+=1
                    matrix[r][c]='-'
                    Santa_presents-=1
                    if Santa_presents ==0:
                        is_ran_out_of_presents=True
                        break
            if is_ran_out_of_presents:
                break
        else:
            matrix[row][col] = 'S'


if nice_kids!=gift_to_nice_kids and is_ran_out_of_presents:
    print("Santa ran out of presents!")
print_matrix(matrix)
if nice_kids==gift_to_nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids-gift_to_nice_kids} nice kid/s.")
