from _collections import deque

start_quantity = int(input())
names = deque()

while True:
    current_command = input()
    if current_command == 'Start':
        break
    names.append(current_command)
command = input()
while command != 'End':
    if command.split()[0] == 'refill':
        extra_water = int(command.split()[1])
        start_quantity += extra_water
    else:
        if start_quantity >= int(command):
            print(f"{names.popleft()} got water")
            start_quantity -= int(command)
        else:
            print(f"{names.popleft()} must wait")

    command = input()
print(f"{start_quantity} liters left")