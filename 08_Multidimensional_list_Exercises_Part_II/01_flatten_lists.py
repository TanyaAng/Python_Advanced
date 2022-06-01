def flatten():
    data = reversed(input().split('|'))
    flatten_matrix = [num.strip() for line in data for num in line.split()]
    return ' '.join(flatten_matrix)

print(flatten())
