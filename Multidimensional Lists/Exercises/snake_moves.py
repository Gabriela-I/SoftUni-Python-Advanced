from collections import deque

rows, columns = [int(el) for el in input().split()]
matrix = deque()
snake = input()
while len(matrix) < rows * columns:
    [matrix.append(ch) for ch in snake if len(matrix) != rows * columns]

for row in range(rows):
    if row % 2 != 0:
        print(*[matrix.popleft() for _ in range(columns)][::-1], sep='')
    else:
        print(*[matrix.popleft() for _ in range(columns)], sep='')


