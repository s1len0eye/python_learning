filename = 'alice.txt'

with open(filename) as file_object:
    contents = file_object.read()
    times = contents.lower().count('the')
    print(str(times))
