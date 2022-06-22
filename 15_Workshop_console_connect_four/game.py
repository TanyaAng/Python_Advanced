from pprint import pprint
from helpers import find_empty_space, is_found_winner
number_rows = 6
number_cols = 7


def main():
    board = [[0] * number_cols for _ in range(number_rows)]
    current_player, oponent = 1, 2

    while True:
        column = int(input(f"Player {current_player} choose column: "))-1
        if column not in range (number_cols):
            print ('Invalid input!')
            continue
        row = find_empty_space(board, column)
        if row == None:
            continue
        board[row][column] = current_player
        pprint(board)
        if is_found_winner(row,column,board):
            print (f"Player {current_player} won the game!")
            exit (0)
        current_player, oponent = oponent, current_player


if __name__ == '__main__':
    main()
