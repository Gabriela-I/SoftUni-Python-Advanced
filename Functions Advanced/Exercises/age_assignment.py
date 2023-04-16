def age_assignment(*names, **ages):
    sorted_names = sorted(names)
    result = []
    for name in sorted_names:
        for k in ages:
            if list(name)[0] == k:
                result.append(f"{name} is {ages[k]} years old.")
    return '\n'.join(result)

print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))