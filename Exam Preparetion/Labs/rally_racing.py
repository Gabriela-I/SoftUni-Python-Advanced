def print_func():
    if finished:
        print(f"Racing car {number_of_car} finished the stage!")
    else:
        print(f"Racing car {number_of_car} DNF.")
    print(f"Distance covered {kilometers} km.")
    for r in race_route:
        print(*r, sep='')


size = int(input())
number_of_car = input()
race_route = []
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1),
}
car_locate = [0, 0]
kilometers = 0
tunnels = []
for row in range(size):
    race_route.append(input().split())
    if 'T' in race_route[row]:
        tunnels.append([row, race_route[row].index('T')])

finished = False

while True:
    command = input()
    if command == 'End':
        race_route[car_locate[0]][car_locate[1]] = 'C'
        break
    car_locate[0], car_locate[1] = car_locate[0] + directions[command][0], car_locate[1] + directions[command][1]

    new_position = race_route[car_locate[0]][car_locate[1]]
    if new_position == 'F':
        kilometers += 10
        race_route[car_locate[0]][car_locate[1]] = 'C'
        finished = True
        break
    elif new_position == 'T':
        tunnels.remove([car_locate[0], car_locate[1]])
        race_route[car_locate[0]][car_locate[1]] = '.'
        car_locate[0], car_locate[1] = tunnels[0][0], tunnels[0][1]
        race_route[car_locate[0]][car_locate[1]] = '.'

        kilometers += 30
        continue
    kilometers += 10


print_func()
