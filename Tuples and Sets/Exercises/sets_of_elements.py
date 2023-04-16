numbers = [int(nums) for nums in input().split()]
first_set = set(int(input()) for n in range(numbers[0]))
second_set = set(int(input()) for h in range(numbers[1]))
same_numbers = first_set.intersection(second_set)
for m in same_numbers:
    print(m)