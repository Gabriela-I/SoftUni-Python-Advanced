row, col = list(map(int, input().split()))
playground = []
my_locate = []
for r in range(row):
    playground.append(input().split())
    if 'B' in playground[r]:
        my_locate = [r, playground[r].index('B')]
        playground[my_locate[0]][my_locate[1]] = '-'

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1),
}

moves = 0
people = 0

while True:
    command = input()
    if command == 'Finish':
        break

    r, c = my_locate[0] + directions[command][0], my_locate[1] + directions[command][1]
    if 0 <= r < row and 0 <= c < col and playground[r][c] != 'O':
        my_locate = [r, c]
        if playground[r][c] == 'P':
            people += 1
            if people == 3:
                moves += 1
                break

        moves += 1
        playground[r][c] = '-'

print("Game over!")
print(f"Touched opponents: {people} Moves made: {moves}")
