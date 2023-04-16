def even_odd(*args):
    command = args[-1]
    if command == 'even':
        return [n for n in args[:-1] if n % 2 == 0]
    else:
        return [n for n in args[:-1] if n % 2 == 1]


print(even_odd(1, 1, 31, 3, 5, 6, "odd"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))


