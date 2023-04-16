def get_sum_of_columns(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    sum_of_columns = []
    for i in range(cols):
        col_sum = 0
        for j in range(rows):
            col_sum += matrix[j][i]
        sum_of_columns.append(col_sum)
    return sum_of_columns


def create_matrix_func():
    matrix = []
    rows, columns = [int(el) for el in input().split(', ')]
    for row in range(rows):
        current_row = [int(el) for el in input().split(' ')]
        matrix.append(current_row)
    return matrix


matrix = create_matrix_func()
result = get_sum_of_columns(matrix)
print(*result, sep='\n')