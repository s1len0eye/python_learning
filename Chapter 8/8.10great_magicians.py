def make_great(names):
    for idx in range(0, len(names)):
        names[idx] = "the Great " + names[idx]
        

def show_magicians(names):
    for name in names:
        print("Magician: " + name.title())

magicians = ['adam', 'bob']
make_great(magicians)
show_magicians(magicians)
