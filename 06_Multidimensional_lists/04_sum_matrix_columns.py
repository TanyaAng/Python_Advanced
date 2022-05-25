def read_matrix():
    n,m=[int(x) for x in input().split(', ')]
    matrix=[]

    for i in range(n):
        row=[int(x) for x in input().split()]
        matrix.append(row)
    return matrix

def sum_matrix_columns(matrix):
    n=len(matrix)
    m=len(matrix[0])
    for col_index in range(m):
        result=0
        for row_index in range(n):
            result+=matrix[row_index][col_index]
        print(result)

matrix=read_matrix()
sum_matrix_columns(matrix)
