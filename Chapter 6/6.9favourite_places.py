favourite_places = {
    'john': ['tokyo', 'england', 'paris'],
    'bob': ['japan', 'italy'],
    'hugo': ['china'],
}

for name, places in favourite_places.items():
    print("The favourite places for " + name.title() + " is :")
    for place in places:
        print("\t" + place.title())
