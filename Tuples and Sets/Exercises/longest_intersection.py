def print_func(longest_i):
    print(f"Longest intersection is [{', '.join(str(x) for x in longest_i)}] with length {len(longest_i)}")



number_of_lines = int(input())
all_intersections = []
longest_intersection = set()
for _ in range(number_of_lines):
    ranges = [i.split(",") for i in input().split('-')]
    first_set = set(range(int(ranges[0][0]), int(ranges[0][1]) + 1))
    second_set = set(range(int(ranges[1][0]), int(ranges[1][1]) + 1))
    result = first_set.intersection(second_set)
    if len(longest_intersection) < len(result):
        longest_intersection = result
print_func(longest_intersection)
