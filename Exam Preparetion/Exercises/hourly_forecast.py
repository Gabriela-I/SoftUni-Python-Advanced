def forecast(*info):
    result = ''
    dict_with_info = {'Sunny': [], 'Cloudy': [], 'Rainy': []}
    for i in info:
        weather = i[1]
        dict_with_info[weather] += [i]
    for v in dict_with_info.values():
        for town in sorted(v):
            result += f'{town[0]} - {town[1]}\n'
    return result


print(forecast(("Sofia", "Sunny"), ("London", "Cloudy"), ("New York", "Sunny")))
print(forecast(("Beijing", "Sunny"), ("Hong Kong", "Rainy"), ("Tokyo", "Sunny"), ("Sofia", "Cloudy"), ("Peru", "Sunny"),
               ("Florence", "Cloudy"), ("Bourgas", "Sunny")))
