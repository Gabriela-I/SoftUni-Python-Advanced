def add(this_stack, num):
    this_stack = this_stack.append(num)
    return this_stack


def delete(this_stack):
    if this_stack:
        this_stack = this_stack.pop()
    return this_stack


def max_num(this_stack):
    if this_stack:
        print(max(this_stack))


def min_num(this_stack):
    if this_stack:
        print(min(this_stack))


def print_stack(this_stack):
    this_stack.reverse()
    print(*this_stack, sep=', ')


lines = int(input())
stack = []
for i in range(lines):
    query = input().split()
    if query[0] == '1':
        add(stack, int(query[1]))
    elif query[0] == '2':
        delete(stack)
    elif query[0] == '3':
        max_num(stack)
    else:
        min_num(stack)


print_stack(stack)


# from collections import deque
#
# numbers = deque()
# map_functions = {
#     1:lambda x: numbers.append(x[1]),
#     2:lambda x: numbers.pop() if numbers else None,
#     3:lambda x: print(max(numbers)) if numbers else None,
#     4:lambda x: print(min(numbers)) if numbers else None,
# }
#
# for _ in range(int(input())):
#     number_data = [int(x) for x in input().split()]
#     map_functions[number_data[0]](number_data)
#
# numbers.reverse()
#
# print(*numbers, sep=', ')