def swap_indexes(row_one, col_one, row_two, col_two):
    matrix[row_one][col_one], matrix[row_two][col_two] = matrix[row_two][col_two], matrix[row_one][col_one]
    for row in matrix:
        print(*row)


def check_indexes(indexes):
    if any([True for i in indexes if i > 0 and i < len(matrix) or i < len(matrix[0])]):
        return True
    return False


rows, columns = [int(el) for el in input().split()]
matrix = [input().split() for row in range(rows)]
while True:
    line = input()
    current_command, *info = [int(x) if x.isdigit() else x for x in line.split()]
    if current_command == 'END':
        break
    elif current_command == 'swap' and len(line.split()) == 5 and check_indexes(info):
        swap_indexes(*info)
    else:
        print('Invalid input!')