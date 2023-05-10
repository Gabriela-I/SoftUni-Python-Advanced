size = int(input())
battlefield = []
submarine = []
for row in range(size):
    battlefield.append(list(input()))
    if 'S' in battlefield[row]:
        submarine = [row, battlefield[row].index('S')]
        battlefield[submarine[0]][submarine[1]] = '-'
counter_of_mines = 0
battle_cruisers = 0
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1),
}
while True:
    way = input()
    submarine = [submarine[0] + directions[way][0], submarine[1] + directions[way][1]]
    if battlefield[submarine[0]][submarine[1]] == '*':
        counter_of_mines += 1
        if counter_of_mines == 3:
            battlefield[submarine[0]][submarine[1]] = 'S'
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine[0]}, {submarine[1]}]!")
            break
    elif battlefield[submarine[0]][submarine[1]] == 'C':
        battle_cruisers += 1
        if battle_cruisers == 3:
            battlefield[submarine[0]][submarine[1]] = 'S'
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

    battlefield[submarine[0]][submarine[1]] = '-'

for row in battlefield:
    print(*row, sep='')