import json

filename = 'favorite_number.json'

try:
    with open(filename) as f_obj:
        number = json.load(f_obj)
except FileNotFoundError:
    with open(filename, 'w') as f_obj:
        number = input("Enter your favorite number: ")
        json.dump(number, f_obj)
else:
    print("I know your favorite number is " + number + ".")
