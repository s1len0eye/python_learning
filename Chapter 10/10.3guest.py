filename = "guest.txt"

with open(filename, 'w') as file_object:
    name = input("Please enter your name: ")
    file_object.write(name)
