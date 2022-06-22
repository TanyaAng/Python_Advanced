def find_empty_space(board, column):
    for row in range(len(board) - 1, -1, -1):
        if board[row][column] == 0:
            return row
    return None


def is_horizontal_winner(board):
    for row in range(len(board) - 1, -1, -1):
        for col in range (0,len(board[row])):
            if board[row][col] in [1,2] and col<=len(board[row])-3:
                if board[row][col+1]==board[row][col] and board[row][col+2]==board[row][col] and board[row][col+3]==board[row][col]:
                    return True
    return False

def is_vertical_winner(board):
    for col in range(7):
        for row in range (len(board) - 1, -1, -1):
            if board[row][col] in [1,2] and row>=3:
                if board[row-1][col]==board[row][col] and board[row-2][col]==board[row][col] and board[row-3][col]==board[row][col]:
                    return True
    return False

def is_primary_diagonal_winner(row,col,board):
    previous_i = row
    previous_j = col
    player_num=board[row][col]
    counter_occurances=1
    for i in range(row - 1, -1, -1):
        for j in range(col - 1, -1, -1):
            if previous_i - 1 == i and previous_j - 1 == j:
                if board[i][j] == player_num:
                    counter_occurances+=1
                    previous_i = i
                    previous_j = j
                    continue
                else:
                    break
    # move by first diagonal down
    previous_i = row
    previous_j = col
    for i in range(row + 1, len(board)):
        for j in range(col + 1, len(board[i])):
            if previous_i + 1 == i and previous_j + 1 == j:
                if board[i][j] == player_num:
                    counter_occurances += 1
                    previous_i = i
                    previous_j = j
                    continue
                else:
                    break
    if counter_occurances == 4:
        return True
    return False

def is_secondary_diagonal_winner (row,col,board):
    previous_i = row
    previous_j = col
    player_num = board[row][col]
    counter_occurances = 1
    for i in range(row - 1, -1, -1):
        for j in range(col + 1, len(board[i])):
            if previous_i - 1 == i and previous_j + 1 == j:
                if board[i][j] == player_num:
                    counter_occurances += 1
                    previous_i = i
                    previous_j = j
                    continue
                else:
                    break
    # move by second diagonal down
    previous_i = row
    previous_j = col
    for i in range(row + 1, len(board)):
        for j in range(col - 1, -1, -1):
            if previous_i + 1 == i and previous_j - 1 == j:
                if board[i][j] == player_num:
                    counter_occurances += 1
                    previous_i = i
                    previous_j = j
                    continue
                else:
                    break
    if counter_occurances == 4:
        return True
    return False


def is_found_winner (row,col,board):
    if is_horizontal_winner(board) or is_vertical_winner(board) or is_primary_diagonal_winner(row,col,board) or is_secondary_diagonal_winner(row,col,board):
        return True
    return False



