from collections import deque

chocolate = deque(int(x) for x in input().split(', '))
milk = deque(int(x) for x in input().split(', '))
shakes = 0
while shakes < 5 and chocolate and milk:
    current_choco = chocolate.pop()
    current_milk = milk.popleft()
    if current_choco <= 0 and current_milk <= 0:
        continue
    elif current_choco <= 0:
        milk.appendleft(current_milk)
        continue
    elif current_milk <= 0:
        chocolate.append(current_choco)
        continue
    if current_choco == current_milk:
        shakes += 1
    elif current_milk != current_choco:
        milk.append(current_milk)
        chocolate.append(current_choco - 5)

if shakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolate:
    print(f"Chocolate:", ', '.join(str(el) for el in chocolate))
else:
    print("Chocolate: empty")
if milk:
    print(f"Milk:", ', '.join(str(x) for x in milk))
else:
    print('Milk: empty')