from _collections import deque

workers = deque(int(x) for x in input().split())
all_nectar = deque(int(x) for x in input().split())
symbols = deque(input().split())
total_honey = 0
operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}
while workers and all_nectar:
    worker = workers.popleft()
    nectar = all_nectar.pop()

    if nectar < worker:
        workers.appendleft(worker)
    elif nectar >= worker:
        current_symbol = symbols.popleft()
        total_honey += abs(operations[current_symbol](worker,nectar))

print(f"Total honey made: {total_honey}")
if workers:
    print(f"Bees left: {', '.join(str(bee) for bee in workers)}")
if all_nectar:
    print(f"Nectar left: {', '.join(str(current_nectar) for current_nectar in all_nectar)}")