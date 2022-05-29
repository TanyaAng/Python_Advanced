def read_square_matrix_and_starting_point(rows):
    matrix = []
    start = tuple()
    for i in range(rows):
        row = []
        line = input().split()
        for j in range(rows):
            row.append(line[j])
            if line[j] == 's':
                start = (i, j)
        matrix.append(row)
    return matrix, start

def find_coals_in_mine(matrix):
    counter=0
    for i in range(len(matrix)):
        for j in range (len(matrix[0])):
            if matrix[i][j]=='c':
                counter+=1
    return counter

rows = int(input())
command = input().split()
matrix, start = read_square_matrix_and_starting_point(rows)
current_i = start[0]
current_j = start[1]
is_game_over=False
for movement in command:
    if movement == 'left':
        if current_j - 1 in range(0, len(matrix)):
            current_j -= 1
    elif movement == 'right':
        if current_j + 1 in range(0, len(matrix)):
            current_j += 1
    elif movement == 'up':
        if current_i - 1 in range(0, len(matrix)):
            current_i -= 1
    elif movement == 'down':
        if current_i + 1 in range(0, len(matrix)):
            current_i += 1

    if matrix[current_i][current_j] == 'c':
        matrix[current_i][current_j] = '*'
    elif matrix[current_i][current_j] == 'e':
        is_game_over=True
        break

if is_game_over:
    print(f"Game over! {(current_i, current_j)}")
else:
    if find_coals_in_mine(matrix)==0:
        print(f"You collected all coal! {(current_i, current_j)}")
    else:
        print(f"{find_coals_in_mine(matrix)} pieces of coal left. {(current_i, current_j)}")


