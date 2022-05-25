def read_matrix():
    n = int(input())
    matrix = [list(input()) for _ in range(n)]
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
