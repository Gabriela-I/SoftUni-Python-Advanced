def shop_from_grocery_list(budget, schedule, *grocery):
    bought_products = {}
    for product in grocery:
        if product[0] in schedule and product[1] <= budget:
            schedule.remove(product[0])
            budget -= float(product[1])
            if product[0] not in bought_products:
                bought_products[product[0]] = 1

        else:
            if product[1] > budget:
                break

    if not schedule:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(schedule)}."




#print(shop_from_grocery_list(100, ["tomato", "cola"], ("cola", 5.8), ("tomato", 10.0), ("tomato", 20.45),))
#print(shop_from_grocery_list(100, ["tomato", "cola", "chips", "meat", "chocolate"], ("cola", 15.8), ("chocolate", 30), ("tomato", 15.85), ("chips", 50), ("meat", 22.99)))
print(shop_from_grocery_list(100, ["tomato", "cola", "chips", "meat"], ("cola", 5.8), ("tomato", 10.0),("meat", 22)))