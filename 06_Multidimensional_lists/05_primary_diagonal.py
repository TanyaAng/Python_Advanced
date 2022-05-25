import sys
from io import StringIO

test_input1 = '''3
11 2 4
4 5 6
10 8 -12
'''

test_input2 = '''3
1 2 3
4 5 6
7 8 9
'''

# sys.stdin=StringIO(test_input1)
# sys.stdin = StringIO(test_input2)


def read_matrix():
    n = int(input())
    matrix = []
    for i in range(n):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix


def get_sum_primary_diagonal(matrix):
    primary_diagonal_sum = 0
    for i in range(len(matrix)):
        primary_diagonal_sum += matrix[i][i]
    return primary_diagonal_sum


def get_sum_secondary_diagonal(matrix):
    n = len(matrix)
    secondary_diagonal_sum = 0
    for i in range(n):
        for j in range(n):
            if i + j == n - 1:
                secondary_diagonal_sum += matrix[i][j]
    return secondary_diagonal_sum

matrix=read_matrix()
print(get_sum_primary_diagonal(matrix))

