from collections import deque


def serving(ramen, customers, bowl, current_customer):
    if bowl > current_customer:
        bowl -= current_customer
        ramen.append(bowl)
    elif current_customer > bowl:
        current_customer -= bowl
        customers.appendleft(current_customer)

    return customers, ramen


ramen_bowl = deque(int(el) for el in input().split(', '))
customers = deque(int(el) for el in input().split(', '))

while ramen_bowl or customers:#!!!!!!!!!!!!
    if not customers or not ramen_bowl:
        break
    current_customer = customers.popleft()
    bowl = ramen_bowl.pop()
    customers, ramen_bowl = serving(ramen_bowl, customers, bowl, current_customer)

if not customers:
    print("Great job! You served all the customers.")
    if ramen_bowl:
        print(f"Bowls of ramen left: {', '.join([str(r) for r in ramen_bowl])}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(r) for r in customers])}")