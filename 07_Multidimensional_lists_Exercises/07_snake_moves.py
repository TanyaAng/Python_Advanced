from collections import deque

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(''.join(str(matrix[i][j]) for j in range(len(matrix[0]))))

rows,cols=[int(x) for x in input().split()]
expression=deque(list(input()))

matrix=[]

for i in range(rows):
    row=deque([])
    for j in range(cols):
        symbol=expression.popleft()
        if i%2==0:
            row.append(symbol)
        else:
            row.appendleft(symbol)
        expression.append(symbol)
    matrix.append(row)

print_matrix(matrix)


