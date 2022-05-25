import sys
from io import StringIO
test_input1='''3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0

'''

test_input2='''3, 3
1 2 3
4 5 6
7 8 9
'''
# sys.stdin=StringIO(test_input1)
sys.stdin=StringIO(test_input2)

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
