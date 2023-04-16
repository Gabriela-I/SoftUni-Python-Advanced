from collections import deque


def math_operations(*numbers, **operators):
    numbers = deque(numbers)
    while numbers:
        current_number = numbers.popleft()
        for k, v in operators.items():
            operators.pop(k)
            if k == 'a':
                v += current_number
            elif k == 'm':
                v *= current_number
            elif k == 's':
                v -= current_number
            elif k == 'd':
                if current_number != 0:
                    v /= current_number
            operators[k] = v
            break
    sorted_operators = dict(sorted(operators.items(), key=lambda x: (-x[1], x[0])))
    result = [f'{k}: {v:.1f}' for k, v in sorted_operators.items()]
    return '\n'.join(result)



print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7,
                      d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-
                                                                    2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
