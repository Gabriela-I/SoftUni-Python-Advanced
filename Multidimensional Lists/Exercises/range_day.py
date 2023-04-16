matrix = []
my_locate = []
shot_targets = []
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1),
}

for row in range(5):
    matrix.append(input().split())
    if 'A' in matrix[row]:
        my_locate = [row, matrix[row].index('A')]
        matrix[row][my_locate[1]] = '.'

number_of_command = int(input())

for _ in range(number_of_command):
    info = input().split()
    command, way = info[0], info[1]
    current_direction = directions[way]

    if command == 'shoot':
        move_r, move_c = my_locate[0] + current_direction[0], my_locate[1] + current_direction[1]
        while 0 <= move_r < len(matrix) and 0 <= move_c < len(matrix):
            if matrix[move_r][move_c] == 'x':
                shot_targets.append([move_r, move_c])
                matrix[move_r][move_c] = '.'
                break

            move_r += current_direction[0]
            move_c += current_direction[1]
    elif command == 'move':
        index = int(info[2])
        r = my_locate[0] + (directions[way][0] * index)
        c = my_locate[1] + (directions[way][1] * index)
        if 0 <= r < len(matrix) and 0 <= c < len(matrix):
            if matrix[r][c] != 'x':
                my_locate = r, c

counter_of_x = 0
for r in range(5):
    if 'x' in matrix[r]:
        counter_of_x += matrix[r].count('x')
if counter_of_x > 0:
    print(f"Training not completed! {counter_of_x} targets left.")
else:
    print(f"Training completed! All {len(shot_targets)} targets hit.")
print(*shot_targets, sep='\n')


