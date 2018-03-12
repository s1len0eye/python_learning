# 我写的代码和题目要求不太一样
sandwich_orders = ['vegetable', 'pastrami', 'meat', 'pastrami', 'fish', 'cheese', 'pastrami', 'fish']
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    if order == 'pastrami':
        print("The deli has run out of pastrami.")
        continue
    print("I made your "+ order + " sandwich.")
    finished_sandwiches.append(order)
    
print("\nSandwiches have been made: ")
for sandwich in finished_sandwiches:
    print(sandwich)

