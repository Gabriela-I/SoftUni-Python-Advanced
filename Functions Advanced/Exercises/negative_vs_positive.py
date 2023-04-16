def check_negative_or_positive(nums):
    positive = []
    negative = []
    for n in nums:
        if n < 0:
            negative.append(n)
        else:
            positive.append(n)

    return sum(positive), sum(negative)


numbers = [int(n) for n in input().split()]
positive_nums, negative_nums = check_negative_or_positive(numbers)
print(negative_nums)
print(positive_nums)
if abs(negative_nums) > positive_nums:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")