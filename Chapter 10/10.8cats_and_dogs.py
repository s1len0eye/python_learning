f_name1 = 'cats.txt'
f_name2 = 'dogs.txt'

try:
    with open(f_name1) as f_obj1:
        contents = f_obj1.read()
        print(contents)
except FileNotFoundError:
    print(f_name1 + " doesn't exist!\n")


try:
    with open(f_name2) as f_obj2:
        contents = f_obj2.read()
        print(contents)
except FileNotFoundError:
    print(f_name2 + " doesn't exist!\n")
