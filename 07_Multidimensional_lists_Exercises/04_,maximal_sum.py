from sys import maxsize

def read_matrix():
    n,m=[int(x) for x in input().split()]
    matrix=[]
    for i in range(n):
        row=[int(x) for x in input().split()]
        matrix.append(row)
    return matrix

def sum_matrix(matrix):
    n=len(matrix)
    m=len(matrix[0])
    total_sum=0
    for i in range (n):
        total_sum+=sum([matrix[i][j] for j in range(m)])
    return total_sum

def print_square_matrix(matrix):
    for i in range(len(matrix)):
        print(' '.join(str(matrix[i][j]) for j in range(len(matrix))))

def find_maximum_square(matrix, square=3):
    n=len(matrix)
    m=len(matrix[0])
    max_sum=-maxsize
    max_square = []
    for i in range (n-(square-1)):
        for j in range(m-(square-1)):
            current_square=[]
            for row in range(square):
                current_square.append([matrix[i+row][j+col] for col in range (square)])
            if sum_matrix(current_square)>max_sum:
                max_sum=sum_matrix(current_square)
                max_square=current_square
    return max_square, max_sum

matrix=read_matrix()
max_square,max_sum=find_maximum_square(matrix)
print(f"Sum = {max_sum}")
print_square_matrix(max_square)