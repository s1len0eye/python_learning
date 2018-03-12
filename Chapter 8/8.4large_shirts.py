
def make_shirt(size='large', message="I love Python"):
    print("The size of the T-shirt is: " + size + ".")
    print("The message printed on the T-shirt is: " + message + ".")
    
make_shirt('small', "first tshirt")
make_shirt(size = 'large', message = "second tshirt")

make_shirt()
make_shirt(size='medium')
make_shirt(size = 'medium', message = 'test')
