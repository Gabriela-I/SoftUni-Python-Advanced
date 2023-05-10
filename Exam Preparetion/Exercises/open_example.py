# def numbers_sum(file_name):
#     data = open(file_name, 'r')
#     sum = 0
#     for num in data:
#         sum += int(num)
#     return sum
#
# print(numbers_sum('open_example.txt'))

# lines = ['I', 'love', 'U', '<3']
#
# with open('love.txt', 'w') as kiss:
#     for line in lines:
#         kiss.write(line)
#         kiss.write('\n')

#
# more_lines = ['Will you marry me?']
# with open('love.txt', 'a') as kiss:
#     kiss.write(*more_lines)

# file = open('my_first_file.txt', 'w')
# file.w('I just created my first file')
# file.close()
#
# from pyfiglet import figlet_format
#
# text = figlet_format('Simona', font='isometric4')
# print(text)

# from modules import convert_text_to_ascii_art
#
# text = 'Simona'
# print(convert_text_to_ascii_art(text))
#
# #
# # from modules import mathematical_operations
# #
# # try:
# #     text = mathematical_operations(*input('Enter first number, operator and second number: ').split())
# #     print(f'Result is: {text:.2f}')
# # except ValueError:
# #     print('Enter a valid data!')
#
# from modules import locate_number, create_sequence
#
#
# def fibonacci_sequence():
#     while True:
#         command = input()
#
#         if command.startswith('Stop'):
#             break
#         elif command.startswith('Create'):
#             print(create_sequence(int(command.split()[2])))
#         elif command.startswith('Locate'):
#             print(locate_number(int(command.split()[1])))
#
#
# fibonacci_sequence()
import io

text = open('open_example.txt', 'r')