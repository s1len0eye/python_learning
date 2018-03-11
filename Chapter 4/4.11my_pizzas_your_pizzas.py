
# Know nothing about pizzas...

colors = ['black', 'white', 'red']
for color in colors:
    print("I love " + color + " color.")
print("I really love colorful things.")

#########################

friend_colors = colors[:]
colors.append('green')
friend_colors.append('silver')

print("\nMy favorite colors are:")
for color in colors:
    print(color)

print("\nMy friend's favorite colors are:")
for color in friend_colors:
    print(color)
