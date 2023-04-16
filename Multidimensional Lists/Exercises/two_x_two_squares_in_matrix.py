def create_matrix_func():
    matrix = [[el for el in input().split()]for _ in range(int(input().split()[0]))]
    return matrix


def get_max_sum():
    matrix = create_matrix_func()
    rows = len(matrix)
    columns = len(matrix[0])
    counter = 0
    for i in range(rows):
        for j in range(columns):
            if i + 1 < len(matrix) and j + 1 < len(matrix[0]):
                if matrix[i][j] == matrix[i][j + 1] and matrix[i][j] == matrix[i + 1][j]\
                    and matrix[i][j] == matrix[i + 1][j + 1]:
                    counter += 1
    return counter


print(get_max_sum())
