# Infinite loop

while(True):
    age = input("Please enter your age: ")
    age = int(age)
    
    if age < 3:
        print("Your ticket is free!\n")
    elif age < 12:
        print("Your ticket is $10.\n")
    else:
        print("Your ticket is $15.\n")
