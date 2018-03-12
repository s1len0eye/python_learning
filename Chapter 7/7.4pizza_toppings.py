prompt = "\nPlease enter the pizza topping you would like to add to your pizza: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    topping = input(prompt)
    
    if topping == 'quit':
        break
    else:
        print("I'll add " + topping.lower() + " to your pizza!")
