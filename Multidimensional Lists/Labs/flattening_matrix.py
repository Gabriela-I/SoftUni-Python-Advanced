rows = int(input())
matrix = []
for row in range(rows):
    current_row = [int(el) for el in input().split(', ')]
    matrix.append(current_row)
result = [num for row in matrix for num in row]
print(result)