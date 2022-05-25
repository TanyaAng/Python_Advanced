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
    max_square=[]
    for i in range (n-1):
        for j in range(m-1):
            if matrix[i][j]+matrix[i][j+1]+matrix[i+1][j]+matrix[i+1][j+1]>max_sum:
                max_sum=matrix[i][j]+matrix[i][j+1]+matrix[i+1][j]+matrix[i+1][j+1]
                max_square=[[matrix[i][j],matrix[i][j+1]],[matrix[i+1][j],matrix[i+1][j+1]]]
    return max_square, max_sum

def print_matrix(matrix):
    for i in range(len(max_square)):
        print(' '.join(str(max_square[i][j]) for j in range(len(max_square))))

matrix=read_matrix()
max_square,max_sum=find_maximum_square(matrix)
print_matrix(max_square)
print(max_sum)


