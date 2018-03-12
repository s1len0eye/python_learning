class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def set_number_served(self, number):
        self.number_served = number
        
    def increment_number_served(self, number):
        self.number_served += number
    
    def describe_restaurant(self):
        print("Restanrant name is: " + self.restaurant_name + ".")
        print("Cuisine type is: " + self.cuisine_type + ".")
        
    def open_restaurant(self):
        print("The restaurant is open.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors=[]):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        
    def show_flavors(self):
        print("Flavors:")
        for flavor in self.flavors:
            print("- " + flavor)

stand = IceCreamStand('sweat', 'france', ['31','23','313'])
stand.show_flavors()
