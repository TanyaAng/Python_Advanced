def read_matrix(size):
    matrix = []
    for _ in range(size):
        matrix.append([x for x in input().split()])
    return matrix

def print_matrix(matrix):
    [print(' '.join(row)) for row in matrix]

Santa_presents=int(input())
neighborhood=int(input())
matrix=read_matrix(neighborhood)
print_matrix(matrix)