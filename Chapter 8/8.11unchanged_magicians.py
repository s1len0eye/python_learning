
def make_great(names):
    for idx in range(0, len(names)):
        names[idx] = "the Great " + names[idx]
    return names
        

def show_magicians(names):
    for name in names:
        print("Magician: " + name.title())

magicians = ['adam', 'bob']
new_magicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(new_magicians)
