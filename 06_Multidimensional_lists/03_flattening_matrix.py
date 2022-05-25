def flatten ():
    n=int(input())
    flatten_matrix=[int(j) for _ in range (n) for j in input().split(', ')]
    return flatten_matrix

print(flatten())