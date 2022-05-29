def read_square_matrix(rows):
    matrix=[]
    for _ in range(rows):
        matrix.append([int(x) for x in input().split(', ')])
    return matrix

def get_primary_diagonal_and_sum(matrix):
    n=len(matrix)
    primary_diagonal=[]
    total_sum=0
    for i in range (n):
        primary_diagonal.append(str(matrix[i][i]))
        total_sum+=matrix[i][i]
    print(f'Primary diagonal: {", ".join(primary_diagonal)}. Sum: {total_sum}')


def get_secondary_diagonal_and_sum(matrix):
    n = len(matrix)
    secondary_diagonal = []
    total_sum = 0
    for i in range(n):
        secondary_diagonal.append(str(matrix[i][n-i-1]))
        total_sum += matrix[i][n-i-1]
    print(f'Secondary diagonal: {", ".join(secondary_diagonal)}. Sum: {total_sum}')

rows=int(input())
matrix=read_square_matrix(rows)
get_primary_diagonal_and_sum(matrix)
get_secondary_diagonal_and_sum(matrix)


