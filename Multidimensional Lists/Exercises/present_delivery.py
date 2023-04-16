number_of_gift = int(input())
size = int(input())
neighbourhood = []
santa_locate = []
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1),
}

count_nice_kids = 0
visited_nice_kids = 0
for row in range(size):
    neighbourhood.append(input().split())
    if 'S' in neighbourhood[row]:
        santa_locate = [row, neighbourhood[row].index('S')]
    if 'V' in neighbourhood[row]:
        count_nice_kids += neighbourhood[row].count('V')

command = input()
while command != 'Christmas morning':
    current_way = directions[command]
    move_r, move_c = santa_locate[0] + current_way[0], santa_locate[1] + current_way[1]
    if 0 <= move_r < size and 0 <= move_c < size:
        neighbourhood[santa_locate[0]][santa_locate[1]] = '-'
        santa_locate = move_r, move_c
        if neighbourhood[move_r][move_c] == 'V':
            number_of_gift -= 1
            visited_nice_kids += 1
        elif neighbourhood[move_r][move_c] == 'C':
            for x, y in directions.values():
                r = move_r + x
                c = move_c + y
                if neighbourhood[r][c].isalpha():
                    if neighbourhood[r][c] == 'V':
                        visited_nice_kids += 1
                    number_of_gift -= 1
                    neighbourhood[r][c] = '-'
                if not number_of_gift:
                    break
        neighbourhood[move_r][move_c] = 'S'
    if not number_of_gift or count_nice_kids == visited_nice_kids:
        break
    command = input()

if number_of_gift == 0 and count_nice_kids != visited_nice_kids:
    print("Santa ran out of presents!")
[print(*r) for r in neighbourhood]
if count_nice_kids == visited_nice_kids:
    print(f"Good job, Santa! {count_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {count_nice_kids - visited_nice_kids} nice kid/s.")