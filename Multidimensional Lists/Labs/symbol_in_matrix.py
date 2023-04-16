def create_matrix_func():
    matrix = []
    rows = int(input())
    for row in range(rows):
        current_row = input()
        matrix.append(current_row)
    return matrix


def find_symbol():
    matrix = create_matrix_func()
    rows = len(matrix)
    columns = len(matrix[0])
    is_find = False
    wanted_symbol = input()
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] is wanted_symbol:
                is_find = True
                return f"({i}, {j})"

    if not is_find:
        return f"{wanted_symbol} does not occur in the matrix"


print(find_symbol())
