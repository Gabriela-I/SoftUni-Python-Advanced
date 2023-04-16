clothes = [int(x) for x in input().split()]
capacity_of_rack = int(input())
sum = 0
number_of_racks = 1
for _ in range(len(clothes)):
    current_cloth = clothes.pop()
    if not sum + current_cloth > capacity_of_rack:
        sum += current_cloth
    else:
        sum = 0
        number_of_racks += 1
        sum += current_cloth

print(number_of_racks)