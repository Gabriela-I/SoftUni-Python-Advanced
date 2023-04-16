def concatenate(*args, **kwargs):
    result = ''.join(args)

    for key in kwargs:
        if key in result:
            result = result.replace(key, kwargs[key])
    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))