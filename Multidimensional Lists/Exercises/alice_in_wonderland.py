def alice_position(ter):
    for row in range(size):
        if "A" in ter[row]:
            col = ter[row].index("A")
            return row, col


def moving_in_territory(a_row, a_col, terr):
    tea_bags = 0
    terr[a_row][a_col] = '*'

    while tea_bags < 10:
        current_command = input()
        move_r, move_c = a_row + directions[current_command][0], a_col + directions[current_command][1]
        if 0 <= move_r < size and 0 <= move_c < size:
            if str(terr[move_r][move_c]).isdigit():
                tea_bags += int(terr[move_r][move_c])
            elif terr[move_r][move_c] == 'R':
                terr[move_r][move_c] = '*'
                print("Alice didn't make it to the tea party.")
                break
            a_row, a_col = move_r, move_c
        else:
            print("Alice didn't make it to the tea party.")
            return tea_bags, terr
        terr[a_row][a_col] = '*'
    return tea_bags, terr


size = int(input())
territory = [[el for el in input().split()] for _ in range(size)]
alice_index = alice_position(territory)
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1),
}
tea, territory = moving_in_territory(*alice_index, territory)
if tea >= 10:
    print("She did it! She went to the party.")
for r in territory:
    print(*r)