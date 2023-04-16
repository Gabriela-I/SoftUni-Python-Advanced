from _collections import deque

paid_command = 'Paid'
end_command = 'End'
customers = deque()

while True:
    command = input()
    if command == paid_command:
        while customers:
            print(customers.popleft())
    elif command == end_command:
        print(f"{len(customers)} people remaining.")
        break
    else:
        customers.append(command)
