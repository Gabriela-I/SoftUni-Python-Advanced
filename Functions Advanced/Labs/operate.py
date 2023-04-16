from functools import reduce


def operate(operator, *args):
    return reduce(lambda x, y: eval(f"{x}{operator}{y}"),args)

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))


# from functools import reduce
#
#
# def operate(operator, *args):
#     def addition(a):
#         return reduce(lambda x, y: x + y, args)
#
#     def subtraction(a):
#         return reduce(lambda x, y: x - y, args)
#
#     def multiplication(a):
#         return reduce(lambda x, y: x * y, args)
#
#     def division(a):
#         return reduce(lambda x, y: x / y, args)
#
#     if operator == '+':
#         return addition(args)
#     elif operator == '-':
#         return subtraction(args)
#     elif operator == '*':
#         return multiplication(args)
#     elif operator == '/':
#         return division(args)