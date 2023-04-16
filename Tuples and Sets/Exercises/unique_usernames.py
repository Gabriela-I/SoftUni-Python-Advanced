number_of_names = int(input())
names = set(input() for _ in range(number_of_names))
for name in names:
    print(name)