#coding=utf-8
people = ['Andy', 'Kelly', 'Julia']

# I prefer to eat alone...
text = "Woule you like to have dinner with me tonight, " 

print(text + people[0] + "?")
print(text + people[1] + "?")
print(text + people[2] + "?")
print("\n")

print(people[2] + " can't make the dinner. So sad :(")
people[2] = 'Linda'

print(text + people[0] + "?")
print(text + people[1] + "?")
print(text + people[2] + "?")
print("\n")

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
print("\n")

######################################

print("Sorry, new table can't arrive on time. I can only invite two people now.")
text2 = " ,I'm sorry to let you know that I can't invite you the the dinner."
name = people.pop()
print(name + text2)
name = people.pop()
print(name + text2)
name = people.pop()
print(name + text2)
name = people.pop()
print(name + text2)
print("\n")

text3 = ", you're still on my inviting list."
print(people[0] + text3)
print(people[1] + text3)
print("\n")

del people[0]
del people[0]  #注意这里！！Index不是1
print(people)
