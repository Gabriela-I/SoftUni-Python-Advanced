def check_valid_coordinate(row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
        return True
    return False


def add(row, col, value):
    matrix[row][col] += value
    return matrix


def subtract(row, col, value):
    matrix[row][col] -= value
    return matrix


matrix = [[int(el) for el in input().split()] for _ in range(int(input()))]
while True:
    command, *data = [int(el) if el.isdigit() or el.lstrip('-').isdigit() else el for el in input().split()]
    if command == 'END':
        break
    elif check_valid_coordinate(data[0], data[1]):
        if command == 'Add':
            add(*data)
        else:
            subtract(*data)
    else:
        print('Invalid coordinates')

for el in matrix:
    print(*el)