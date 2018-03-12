cars = ['audi', 'BMW', 'subaru', 'toyota']
numbers = [3, 54, 12, 6, 134]

for car in cars:
    if car.lower() == "subaru":
        print("There is sucaru in the list.")

low = 0
high = 0
for number in numbers:
    if number > 10:
        high += 1
    else:
        low += 1
print("There are " + str(high) + " numbers greater than 10.")

for number in numbers:
    if number >= 5 and number <= 10:
        print("The list has number between 5 and 10.")

if 'subaru' in cars:
    print("There is sucaru in the list.")

if '324' not in cars:
    print("There is no 324 in the list.")
