rows, columns = [int(el) for el in input().split(', ')]
matrix = []
total_sum = 0
for row in range(rows):
    current_row = [int(el) for el in input().split(', ')]
    matrix.append(current_row)
    for col in range(columns):
        total_sum += current_row[col]
print(total_sum)
print(matrix)