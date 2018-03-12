sandwich_orders = ['vegetable', 'meat', 'fish', 'cheese', 'fish']
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    print("I made your "+ order + " sandwich.")
    finished_sandwiches.append(order)
    
print("\nSandwiches have been made: ")
for sandwich in finished_sandwiches:
    print(sandwich)
