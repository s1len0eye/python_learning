filename = 'learning_python.txt'

with open(filename) as file_object:
    #lines = file_object.readlines()
    #contents = file_object.read()
    for line in file_object:
        print(line)
    #print(contents.rstrip())
    
#for line in lines:
#    print(line)
        

