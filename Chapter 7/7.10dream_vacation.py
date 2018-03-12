vacations = {}

active = True

while active:
    print("\nUsing 'quit' to exit.")
    name = input("What's your name? ")
    if name == 'quit':
        break
    vacation = input("If you could visit one place in the world, where would you go? ")
    if vacation == 'quit':
        break
    
    vacations[name] = vacation
    
for name, vacation in vacations.items():
    print("\n" + name.title() + " want to go to " + vacation + " for a vcation.")
