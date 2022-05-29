def read_square_matrix(rows):
    matrix=[]
    for _ in range(rows):
        matrix.append([int(x) for x in input().split()])
    return matrix

def get_primary_diagonal_sum(matrix):
    n=len(matrix)
    total_sum=0
    for i in range (n):
        total_sum+=matrix[i][i]
    return total_sum


def get_secondary_diagonal_sum(matrix):
    n = len(matrix)
    total_sum = 0
    for i in range(n):
        total_sum += matrix[i][n-i-1]
    return total_sum

rows=int(input())
matrix=read_square_matrix(rows)
print(abs(get_primary_diagonal_sum(matrix)-get_secondary_diagonal_sum(matrix)))