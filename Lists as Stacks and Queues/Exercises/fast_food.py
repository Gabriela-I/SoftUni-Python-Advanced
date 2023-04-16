from collections import deque

quantity_food = int(input())
all_orders = deque([int(n) for n in input().split()])
print(max(all_orders))
is_succeeded = True
while all_orders:
    current_order = int(all_orders[0])
    if quantity_food >= current_order:
        quantity_food -= current_order
        all_orders.popleft()
    else:
        is_succeeded = False
        break

if is_succeeded:
    print('Orders complete')
else:
    print(f"Orders left: ", end='')
    print(*all_orders, sep=' ')