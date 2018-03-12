from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides
        
    def roll_die(self):
        print(randint(1, self.sides))

die = Die()
for dummy in range(0, 10):
    die.roll_die()

print("\n")
die = Die(10)
for dummy in range(0, 10):
    die.roll_die()

print("\n")
die = Die(20)
for dummy in range(0, 10):
    die.roll_die()
