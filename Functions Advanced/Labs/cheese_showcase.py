def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda n: (-len(n[1]), n[0]))

    def sorted_quantities(cheeses):
        result = []
        for cheese_name, quantity in cheeses:
            result.append(cheese_name)
            result.extend(sorted(quantity, reverse=True))
        return '\n'.join(str(el) for el in result)
    return sorted_quantities(sorted_cheeses)


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)