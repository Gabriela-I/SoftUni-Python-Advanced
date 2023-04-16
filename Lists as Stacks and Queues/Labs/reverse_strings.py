text = list(input())
stack = []
while len(text) > 0:
    element = stack.append(text.pop())
print(''.join(stack))


# stack = list(input())
# for i in range(len(stack)):
#     element = stack.pop()
#     print(element, end='')