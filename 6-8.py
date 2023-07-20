# TODO Дан словарь, ключ - Название страны, значение - список городов, на вход поступает город,
#  необходимо сказать из какой он страны.


data = {
    'Belarus': ['Minsk', 'Brest'],
    'Poland': ['Warczawa', 'Krakow'],
    'USA': ['Woshington', 'LA'],
    'UK': ['London', 'Cambridge']
}
city = input('Type city:')


def geography(a, b):
    for key, value in a.items():
        if b in value:
            return key


print(geography(data, city))
