filename = "responses.txt"

with open(filename, 'a') as file_object:
    while True:
        response = input("Why do you like programming('q' to exit)? ")
        if response == 'q':
            break
        else:
            file_object.write(response + "\n")
