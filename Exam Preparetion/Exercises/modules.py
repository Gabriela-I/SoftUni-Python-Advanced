# from pyfiglet import figlet_format
#
#
# def convert_text_to_ascii_art(text):
#     result = figlet_format(text, font='5lineoblique')
#     return result
#
#
# print(convert_text_to_ascii_art('ivan'))

# import operator as op
#
#
# def mathematical_operations(first_number, operator, second_number):
#     first_number, second_number = int(first_number), int(second_number)
#     valid_operators = {'+': op.add, '-': op.sub, '*': op.mul, '^': op.xor, '/': op.truediv}
#
#     return valid_operators[operator](first_number, second_number)


sequence_of_numbers = []


def create_sequence(number):
    sequence_of_numbers.clear()
    sequence_of_numbers.append(0)
    sequence_of_numbers.append(1)

    for _ in range(number - 2):
        sequence_of_numbers.append(sequence_of_numbers[-1] + sequence_of_numbers[-2])

    return ' '.join(map(str, sequence_of_numbers))


def locate_number(element):
    if element in sequence_of_numbers:
        element_index = sequence_of_numbers.index(element)
        return f'The number - {element} is at index {element_index}'
    else:
        return f'The number - {element} is not in the sequence'