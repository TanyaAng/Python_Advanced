def read_matrix():
    n, m = [int(x) for x in input().split()]
    matrix = []
    for i in range(n):
        matrix.append(input().split())
    return matrix


def is_in_matrix_range(matrix,*args):
    n=len(matrix)
    m=len(matrix[0])
    for i in range (len(args)):
        if args[i] < 0:
            return False
        if i%2==0:
            if args[i] not in range(n):
                return False
        else:
            if args[i] not in range(m):
                return False
    return True


def print_matrix(matrix):
    for i in range(len(matrix)):
        print(' '.join(str(matrix[i][j]) for j in range(len(matrix[0]))))


matrix = read_matrix()

while True:
    command = input()
    if command == 'END':
        break
    data = command.split()
    if len(data)!=5:
        print('Invalid input!')
        continue
    else:
        if data[0] == 'swap' and is_in_matrix_range(matrix, int(data[1]), int(data[2]), int(data[3]),
                                                     int(data[4])):
            matrix[int(data[1])][int(data[2])], matrix[int(data[3])][int(data[4])] = matrix[int(data[3])][int(data[4])], \
                                                                                     matrix[int(data[1])][int(data[2])]
            print_matrix(matrix)

        else:
            print('Invalid input!')


