active = True

while(active):
    age = input("Please enter your age('quit' to exit): ")
    
    if age == 'quit':
        break
    
    age = int(age)

    if age > 120:
        print("You must be kidding.\n")
        active = False
    elif age < 3:
        print("Your ticket is free!\n")
    elif age < 12:
        print("Your ticket is $10.\n")
    else:
        print("Your ticket is $15.\n")
