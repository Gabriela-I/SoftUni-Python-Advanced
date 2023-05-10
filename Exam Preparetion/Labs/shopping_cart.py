def shopping_cart(*info):
    def making_dict():
        nonlocal dict_with_meals, with_products
        meal = pair[0]
        product = pair[1]
        if len(dict_with_meals[meal]) < limit_of_products[meal] and product not in dict_with_meals[meal]:
            with_products = True
            dict_with_meals[meal].append(product)
        return dict_with_meals
    with_products = False
    limit_of_products = {
        'Soup': 3,
        'Pizza': 4,
        'Dessert': 2,
    }
    dict_with_meals = {'Soup': [], 'Pizza': [], 'Dessert': []}
    for pair in info:
        if pair == 'Stop':
            if not with_products:
                return "No products in the cart!"
            else:
                output = ''
                result = dict(sorted(dict_with_meals.items(), key=lambda x: (-len(x[1]), x[0])))
                for m, p in result.items():
                    output += f'{m}:\n'
                    for el in sorted(p):
                        output += f' - {el}\n'
                return output
        making_dict()



print(shopping_cart(

    ('Pizza', 'ham'),

    ('Soup', 'carrots'),

    ('Pizza', 'cheese'),

    ('Pizza', 'flour'),

    ('Dessert', 'milk'),

    ('Pizza', 'mushrooms'),

    ('Pizza', 'tomatoes'),

    'Stop', ))
#print(shopping_cart('Stop',('Pizza', 'ham'),('Pizza', 'mushrooms'),))
#print(shopping_cart(('Pizza', 'ham'),('Dessert', 'milk'),('Pizza', 'ham'), 'Stop', ))