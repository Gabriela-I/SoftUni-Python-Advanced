def grocery_store(**schedule):
    sorted_schedule = dict(sorted(schedule.items(), key=lambda n: (-n[1], -len(n[0]), n[0])))
    result = [f'{k}: {v}' for k, v in sorted_schedule.items()]
    return '\n'.join(result)

print(grocery_store(

    bread=5,

    pasta=12,

    eggs=12,

))
print(grocery_store(

    bread=2,

    pasta=2,

    eggs=20,

    carrot=1,

))