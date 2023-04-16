from collections import deque

petrol_in_tank = 0
index = 0
all_pumps = deque([[int(x) for x in input().split()] for i in range(int(input()))])
copy_of_all_pumps = all_pumps.copy()
while copy_of_all_pumps:
    amount_of_petrol, distance = copy_of_all_pumps.popleft()
    if petrol_in_tank + amount_of_petrol >= distance:
        petrol_in_tank += amount_of_petrol
        petrol_in_tank -= distance
    else:
        all_pumps.rotate(-1)
        copy_of_all_pumps = all_pumps.copy()
        index += 1
        petrol_in_tank = 0
print(index)

