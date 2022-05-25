import sys
from sys import maxsize

def read_matrix():
    n,m=[int(x) for x in input().split(', ')]
    matrix=[]
    for i in range(n):
        row=[int(x) for x in input().split(', ')]
        matrix.append(row)
    return matrix

def find_maximum_square(matrix):
    n=len(matrix)
    m=len(matrix[0])
    max_sum=-sys.maxsize
    for i in range (n-1):
        for j in range(m-1):
            if matrix[i][j]+matrix[i][j+1]+matrix[i+1][j]+matrix[i+1][j+1]>=max_sum:
                max_square=[[matrix[i][j],matrix[i][j+1]],matrix[i+1][j],matrix[i+1][j+1]]
                return max_square

matrix=read_matrix()
print(find_maximum_square(matrix))


