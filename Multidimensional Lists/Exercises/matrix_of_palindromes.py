rows, columns = [int(el) for el in input().split()]
matrix = []
start_a = ord('a')

for row in range(rows):
    for col in range(columns):
        print(chr(row + start_a) + chr(row + col + start_a) + chr(row + start_a), end=' ')
    print()
