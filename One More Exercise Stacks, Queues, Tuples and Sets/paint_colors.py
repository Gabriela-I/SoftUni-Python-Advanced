import math

data = input().split()
colors = {'red', 'yellow', 'purple', 'orange', 'blue', 'green'}
req_colors = {
    'purple': {'red', 'blue'},
    'orange': {'red', 'yellow'},
    'green': {'yellow', 'blue'},
}
result = []

while data:
    first_part = data.pop(0)
    last_part = data.pop() if data else ''
    combination = first_part + last_part
    reversed_comb = last_part + first_part

    for color in (combination, reversed_comb):
        if color in colors:
            result.append(color)
            break
    else:
        middle_of_data = math.ceil(len(data) / 2)
        for el in (first_part[:-1], last_part[:-1]):
            if el:
                data.insert(middle_of_data, el)

for color in set(req_colors.keys()).intersection(result):
    if not req_colors[color].issubset(result):
        result.remove(color)

print(result)