import sys

size = int(input())
field = [[el for el in input().split()] for row in range(size)]
directions = ['up', 'right', 'down', 'left']
max_eggs = - sys.maxsize
way = ''
pos = ''
for row in range(size):
    for col in range(size):
        current_index = field[row][col]
        if current_index == 'B':
            for d in directions:
                eggs = 0
                positions = []
                if d == 'up':
                    if row == 0:
                        continue
                    for i in range(row - 1, -1, -1):
                        if field[i][col] == 'X':
                            break
                        eggs += int(field[i][col])
                        positions.append([i, col])
                    if eggs >= max_eggs:
                        max_eggs = eggs
                        way = d
                        pos = positions
                elif d == 'right':
                    if col == size:
                        continue
                    for i in range(col + 1, size):
                        if field[row][i] == 'X':
                            break
                        eggs += int(field[row][i])
                        positions.append([row, i])
                    if eggs >= max_eggs:
                        max_eggs = eggs
                        way = d
                        pos = positions
                elif d == 'down':
                    if row == size:
                        continue
                    for i in range(row + 1, size):
                        if field[i][col] == 'X':
                            break
                        eggs += int(field[i][col])
                        positions.append([i, col])
                    if eggs >= max_eggs:
                        max_eggs = eggs
                        way = d
                        pos = positions
                else:
                    if col == 0:
                        continue
                    for i in range(col - 1, -1, -1):
                        if field[row][i] == 'X':
                            break
                        eggs += int(field[row][i])
                        positions.append([row, i])
                    if eggs >= max_eggs:
                        max_eggs = eggs
                        way = d
                        pos = positions

print(way)
print(*pos, sep='\n')
print(max_eggs)