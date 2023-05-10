def lets_play(chessboard):
    for course in range(0, 9):
        if course % 2 == 0:
            current_move = white
        else:
            current_move = black
        possible_attacks = [[-1, -1], [-1, 1], [1, 1], [1, -1]]

        for attack in possible_attacks:
            if 0 <= current_move[0][0] + attack[0] < 8 and 0 <= current_move[0][1] + attack[1] < 8:
                if chessboard[current_move[0][0] + attack[0]][current_move[0][1] + attack[1]].isalpha():
                    return f"Game over! {current_move[1]} win, capture on " \
                           f"{copy_board[current_move[0][0] + attack[0]][current_move[0][1] + attack[1]]}."

        current_move[0][0] += current_move[2]
        chessboard[current_move[0][0]][current_move[0][1]] = current_move[4]
        if current_move[0][0] == current_move[3]:
            return f"Game over! {current_move[1]} pawn is promoted to a queen at " \
                   f"{copy_board[current_move[0][0]][current_move[0][1]]}."


chessboard = []
white_locate = []
black_locate = []
copy_board = []
for col in range(8, 0, -1):
    this_row = []
    for row in range(97, 105):
        this_row.append(f'{chr(row)}{col}')
    copy_board.append(this_row)

for row in range(8):
    chessboard.append(input().split())
    if 'w' in chessboard[row]:
        white_locate = [row, chessboard[row].index('w')]
    if 'b' in chessboard[row]:
        black_locate = [row, chessboard[row].index('b')]

up = -1
down = 1
white = [white_locate, 'White', up, 0, 'w']
black = [black_locate, 'Black', down, 7, 'b']

print(lets_play(chessboard))


