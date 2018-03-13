filename = "guest_book.txt"

with open(filename, 'w') as file_object:
    while True:
        name = input("Enter your name('q' to quit): ")
        if name == 'q':
            break
        else:
            print("Hello, " + name + ".\n")
            file_object.write(name + " visit. \n")
