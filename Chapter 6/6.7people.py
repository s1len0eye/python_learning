person1 = {'first_name': 'Hugo',
    'last_name': 'Chan',
    'age': 24,
    'country': 'China',
}
person2 = {'first_name': 'Bob',
    'last_name': 'White',
    'age': 33,
    'country': 'US',
}
person3 = {'first_name': 'Tom',
    'last_name': 'Black',
    'age': 18,
    'country': 'UK',
}
persons = [person1, person2, person3]

for person in persons:
    for key, value in person.items():
        print(key + ": " + str(value))
    print("\n")
