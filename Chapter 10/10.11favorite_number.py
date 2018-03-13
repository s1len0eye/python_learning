import json

filename = 'favorite_number.json'

with open(filename, 'w') as f_obj:
    number = input("Enter your favorite number: ")
    json.dump(number, f_obj)
