from functools import reduce

exercise = input().split()
result = []

for el in exercise:
    if el == '*':
        result = [reduce((lambda x, y: x * y), result)]
    elif el == '+':
        result = [reduce((lambda x, y: x + y), result)]
    elif el == '-':
        result = [reduce((lambda x, y: x - y), result)]
    elif el == '/':
        result = [reduce((lambda x, y: x // y), result)]
    else:
        result.append(int(el))
print(*result)