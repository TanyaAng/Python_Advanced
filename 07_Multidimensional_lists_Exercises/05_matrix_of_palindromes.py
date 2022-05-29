def get_matrix_of_palindromes(rows, cols):
    STARTING_CHAR=ord('a')
    matrix=[]
    for i in range(rows):
        current_row=[]
        for j in range(cols):
            current_row.append(chr(STARTING_CHAR+i)+chr(STARTING_CHAR+i+j)+chr(STARTING_CHAR+i))
        matrix.append(current_row)
    return print_matrix(matrix)

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(' '.join(str(matrix[i][j]) for j in range(len(matrix[0]))))

rows, cols = [int(x) for x in input().split()]
get_matrix_of_palindromes(rows,cols)
