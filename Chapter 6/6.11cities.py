cities = {
    'tokyo': {
        'country': 'japan',
        'population': 23,
        'fact': 'nothing',
    },
    'milan': {
        'country': 'italy',
        'population': 32,
        'fact': 'nothing',
    },
    'london': {
        'country': 'UK',
        'population': 42,
        'fact': 'nothing'
    },
}

for city, informations in cities.items():
    print(city + ": ")
    for key, value in informations.items():
        print("\t" + key + ": \n\t\t" + str(value))
