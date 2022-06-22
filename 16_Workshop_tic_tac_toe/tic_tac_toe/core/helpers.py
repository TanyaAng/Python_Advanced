from tic_tac_toe.core.constants import position_mapper


def get_row_col(pos):
    return position_mapper[pos]

def print_current_board_state(board):
    [print (f"| {' | '.join (el)} |") for el in board]


def is_board_full(board):
    is_full=True
    for row in board:
        if ' ' in row:
            is_full=False
            break
    return is_full

def is_row_winner (board):
    is_found=False
    for row in board:
        if row.count('X')==len(row) or row.count('O')==len(row):
            is_found=True
    return is_found

def is_col_winner (board):
    is_found=False
    for col in range(len(board)):
        current_col=[]
        for row in range (len(board)):
            current_col.append(board[row][col])
        if current_col.count('X')==len(board) or current_col.count('O')==len(board):
            is_found=True
            break
    return is_found

def is_primary_diagonal_winner (board):
    is_found=False
    current_values=[]
    for row in range (len(board)):
        current_values.append(board[row][row])
    if current_values.count('X')==len(board) or current_values.count('O')==len(board):
        is_found=True
    return is_found

def is_secondary_diagonal_winner (board):
    is_found=False
    current_values=[]
    for row in range (len(board)):
        for col in range (len(board)):
            if row+col==len(board)-1:
                current_values.append(board[row][col])
    if current_values.count('X')==len(board) or current_values.count('O')==len(board):
        is_found=True
    return is_found


def is_winner(board):
    if is_row_winner(board) or is_col_winner(board) or is_primary_diagonal_winner(board) or is_secondary_diagonal_winner(board):
        return True
    return False
