def read_matrix():
    n,m=[int(x) for x in input().split()]
    matrix=[]
    for i in range(n):
        row=input().split()
        matrix.append(row)
    return matrix

def find_maximum_square(matrix):
    n=len(matrix)
    m=len(matrix[0])
    counter=0
    for i in range (n-1):
        for j in range(m-1):
            if matrix[i][j]==matrix[i][j+1]==matrix[i+1][j]==matrix[i+1][j+1]:
                counter+=1
    return counter

matrix=read_matrix()
print(find_maximum_square(matrix))
