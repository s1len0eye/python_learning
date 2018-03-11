people = ['Andy', 'Kelly', 'Julia']

# I prefer to eat alone...
text = "Woule you like to have dinner with me tonight, " 

print(text + people[0] + "?")
print(text + people[1] + "?")
print(text + people[2] + "?")

print(people[2] + " can't make the dinner. So sad :(")
people[2] = 'Linda'

print(text + people[0] + "?")
print(text + people[1] + "?")
print(text + people[2] + "?")

#################################

print("Good news everyone, I have found a bigger table for our dinner tonight.")
people.insert(0, 'Angel')
people.insert(2, 'Ann')
people.append('Bob')

print(text + people[0] + "?")
print(text + people[1] + "?")
print(text + people[2] + "?")
print(text + people[3] + "?")
print(text + people[4] + "?")
print(text + people[5] + "?")
