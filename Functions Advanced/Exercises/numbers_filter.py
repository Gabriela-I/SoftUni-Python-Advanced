def even_odd_filter(**kwargs):
    for key in kwargs:
        if key == 'odd':
            kwargs[key] = list(filter(lambda x: x % 2 != 0, kwargs[key])) # [n for n in kwargs[key] if n % 2 == 1]
        else:
            kwargs[key] = list(filter(lambda x: x % 2 == 0, kwargs[key]))

    return dict(sorted(kwargs.items(), key=lambda n: len(n[1]), reverse=True))


print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5],even=[3, 4, 5, 7, 10, 2, 5, 5, 2],))
print(even_odd_filter(odd=[2, 2, 30, 44, 10, 5],))