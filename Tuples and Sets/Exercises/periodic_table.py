number_of_elements = int(input())
unique_names = set()
for n in range(number_of_elements):
    elements = input().split()
    for el in elements:
        unique_names.add(el)
for e in unique_names:
    print(e)