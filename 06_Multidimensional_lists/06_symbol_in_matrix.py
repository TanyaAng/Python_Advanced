def read_matrix():
    n = int(input())
    matrix = []
    for i in range(n):
        row = [x for x in list(input())]
        matrix.append(row)
    return matrix

def find_indexes_of_current_element(matrix, element):
    for i in range (len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]==element:
                return (i,j)

    return f"{symbol} does not occur in the matrix"

matrix=read_matrix()
symbol=input()
print(find_indexes_of_current_element(matrix, symbol))
