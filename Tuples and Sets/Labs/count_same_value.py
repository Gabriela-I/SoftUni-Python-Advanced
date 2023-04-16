numbers = tuple(map(float, input().split()))
counter = {}
for num in numbers:
    if num not in counter:
        counter[num] = 0
    counter[num] += 1

for k, v in counter.items():
    print(f"{k} - {v} times")