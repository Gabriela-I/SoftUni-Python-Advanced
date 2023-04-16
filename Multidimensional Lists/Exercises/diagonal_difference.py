rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

primary, secondary = 0, 0

for i in range(rows):
    primary += matrix[i][i]
    secondary += matrix[rows - i - 1][i]

print(abs(primary - secondary))
