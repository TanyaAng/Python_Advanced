def read_and_sum_matrix():
    n,m=[int(x) for x in input().split(', ')]

    matrix=[]
    total_sum=0
    for i in range(n):
        row=[int(x) for x in input().split(', ')]
        total_sum+=sum(row)
        matrix.append(row)
    return matrix, total_sum

matrix,total_sum=read_and_sum_matrix()
print(total_sum)
print(matrix)
