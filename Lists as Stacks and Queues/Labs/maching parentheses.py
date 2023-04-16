exercise = input()
parentheses = []
for i in range(len(exercise)):
    if exercise[i] == '(':
        parentheses.append(i)
    elif exercise[i] == ')':
        start = parentheses.pop()
        end = i + 1
        print(exercise[start:end])
