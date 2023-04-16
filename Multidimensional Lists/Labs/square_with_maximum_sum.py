from sys import maxsize


def create_matrix_func():
    matrix = []
    rows = int(input().split(', ')[0])
    for row in range(rows):
        current_row = [int(el) for el in input().split(', ')]
        matrix.append(current_row)
    return matrix


def get_max_sum():
    matrix = create_matrix_func()
    rows = len(matrix)
    columns = len(matrix[0])
    max_sum = -maxsize
    max_values = []
    for i in range(rows):
        for j in range(columns):
            if i + 1 < len(matrix) and j + 1 < len(matrix[0]):
                sub_matrix = [matrix[i][j], matrix[i][j + 1], matrix[i + 1][j], matrix[i + 1][j + 1]]
                if sum(sub_matrix) > max_sum:
                    max_sum = sum(sub_matrix)
                    max_values = sub_matrix
    return max_values


result = get_max_sum()
print(f'{result[0]} {result[1]}')
print(f'{result[2]} {result[3]}')
print(sum(result))