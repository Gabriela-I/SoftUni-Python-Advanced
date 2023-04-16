def recursive_power(first_num, second_num):
    if second_num == 0:
        return 1
    if second_num == 1:
        return first_num
    return first_num * recursive_power(first_num, second_num - 1)


print(recursive_power(2, 10))