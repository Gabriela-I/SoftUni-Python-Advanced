size = int(input())
board = [list(input()) for row in range(size)]
removed_knights = 0
possible_moves = [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2]]

while True:
    knight_with_most_attacks = []
    max_attacks = 0
    for row in range(size):
        for col in range(size):
            current_index = board[row][col]
            if current_index == 'K':
                attacks = 0
                for move in possible_moves:
                    r = row + move[0]
                    c = col + move[1]
                    if 0 <= r < size and 0 <= c < size:
                        if board[r][c] == 'K':
                            attacks += 1
                if attacks > max_attacks:
                    knight_with_most_attacks = [row, col]
                    max_attacks = attacks
    if knight_with_most_attacks:
        board[knight_with_most_attacks[0]][knight_with_most_attacks[1]] = 0
        removed_knights += 1
    else:
        break
print(removed_knights)