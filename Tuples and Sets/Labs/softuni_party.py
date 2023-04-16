def arrived_guests():
    arrived = []
    while True:
        command = input()
        if command == 'END':
            break
        else:
            arrived.append(command)
    return arrived


def print_guests(not_arrived):
    print(len(not_arrived_guests))
    for gu in sorted(not_arrived_guests):
        print(gu)


number_of_guests = int(input())
guests = [input() for _ in range(number_of_guests)]
arrived_guests_data = arrived_guests()
not_arrived_guests = set(guests).difference(arrived_guests_data)
print_guests(not_arrived_guests)