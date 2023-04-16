def create_matrix_func(rows):
    matrix = [[int(el) for el in input().split(', ')] for _ in range(rows)]
    return matrix


def get_primary_diagonal(matrix):
    primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
    return primary_diagonal


def get_secondary_diagonal(matrix):
    secondary_diagonal = [matrix[(len(matrix) - 1) - j][j] for j in range(len(matrix) - 1, -1, -1)]
    return secondary_diagonal


rows = int(input())
matrix = create_matrix_func(rows)
result_one = get_primary_diagonal(matrix)
print(f"Primary diagonal: {', '.join(str(el) for el in result_one)}. Sum: {sum(result_one)}")

result_two = get_secondary_diagonal(matrix)
print(f"Secondary diagonal: {', '.join([str(el) for el in result_two])}. Sum: {sum(result_two)}")