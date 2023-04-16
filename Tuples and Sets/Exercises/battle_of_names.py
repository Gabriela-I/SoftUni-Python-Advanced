def print_func(odd, even):
    if sum(odd) > sum(even):
        print(*odd.difference(even), sep=', ')
    elif sum(odd) == sum(even):
        print(*odd.union(even), sep=', ')
    else:
        print(*odd.symmetric_difference(even), sep=', ')


number_of_names = int(input())
odd_set = set()
even_set = set()
for i in range(1, number_of_names + 1):
    current_name = sum([ord(char) for char in input()])
    if (int(current_name/i)) % 2 == 0:
        even_set.add(int(current_name/i))
    else:
        odd_set.add(int(current_name/i))

print_func(odd_set, even_set)
