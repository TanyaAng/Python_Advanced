def find_count(board, row, col):
    counter=0
    moves=[
        [row-2,col-1],
        [row-2, col+1],
        [row-1, col-2],
        [row-1, col+2],
        [row+1, col-2],
        [row+1, col+2],
        [row+2, col-1],
        [row+2, col+1]
    ]
    for r,c in moves:
        if r in range(len(board)) and c in range(len(board)) and board[r][c]=='K':
            counter+=1
    return counter




size = int(input())
board = []
for _ in range(size):
    board.append(list(input()))

removed_knight = 0
while True:
    best_count = 0
    knight_row = 0
    knight_col = 0
    for row in range(size):
        for col in range(size):
            if board[row][col] == '0':
                continue
            count = find_count(board, row, col)
            if count > best_count:
                best_count = count
                knight_row = row
                knight_col = col
    if best_count == 0:
        break

    board[knight_row][knight_col] = '0'
    removed_knight += 1

print(removed_knight)
