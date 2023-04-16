first_sequences = set(int(x) for x in input().split())
second_sequences = set(int(x) for x in input().split())
number_of_commands = int(input())
for _ in range(number_of_commands):
    command, *data = input().split()

    current_command = command + ' ' + data.pop(0)
    if current_command == 'Add First':
        [first_sequences.add(int(el))for el in data]
    elif current_command == 'Add Second':
        [second_sequences.add(int(el))for el in data]
    elif current_command == 'Remove First':
        [first_sequences.discard(int(el)) for el in data]
    elif current_command == 'Remove Second':
        [second_sequences.discard(int(el)) for el in data]
    else:
        if first_sequences.issubset(second_sequences) or second_sequences.issubset(first_sequences):
            print('True')
        else:
            print('False')

print(*sorted(first_sequences), sep=', ')
print(*sorted(second_sequences), sep=', ')