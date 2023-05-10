from collections import deque

textiles = deque([int(el) for el in input().split()])
medicaments = deque([int(el) for el in input().split()])

product = {}
elements = {30: 'Patch', 40: 'Bandage', 100: 'MedKit'}

while True:
    if not textiles or not medicaments:  # !!!!!!!!!!!!!!!
        break
    current_textile = textiles.popleft()
    this_medicament = medicaments.pop()

    if current_textile + this_medicament in elements:
        if elements[current_textile + this_medicament] not in product:
            product[elements[current_textile + this_medicament]] = 0
        product[elements[current_textile + this_medicament]] += 1

    elif current_textile + this_medicament > 100:
        if elements[100] not in product:
            product[elements[100]] = 0
        product[elements[100]] += 1
        next_med = medicaments.pop()
        next_med += (current_textile + this_medicament) - 100
        medicaments.append(next_med)

    elif current_textile + this_medicament < 100:
        medicaments.append(this_medicament + 10)


if medicaments:
    print("Textiles are empty.")
elif textiles:
    print("Medicaments are empty.")
elif not medicaments and not textiles:
    print("Textiles and medicaments are both empty.")

if product:
    sorted_products = dict(sorted(product.items(), key=lambda x: (-x[1], x[0])))
    for k, v in sorted_products.items():
        print(f'{k} - {v}')

if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")
if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(map(str, medicaments))}")