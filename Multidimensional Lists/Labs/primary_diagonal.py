def create_matrix_func():
    matrix = []
    rows = int(input())
    for row in range(rows):
        current_row = [int(el) for el in input().split(' ')]
        matrix.append(current_row)
    return matrix


def get_sum_of_primary_diagonal():
    matrix = create_matrix_func()
    sum_of_primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
    return sum(sum_of_primary_diagonal)


print(get_sum_of_primary_diagonal())

# number_of_rows = int(input())
# sum = 0
# for i in range(number_of_rows):
#     current_row = [int(el) for el in input().split()]
#     sum += current_row[i]
# print(sum)