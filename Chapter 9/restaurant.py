class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print("Restanrant name is: " + self.restaurant_name + ".")
        print("Cuisine type is: " + self.cuisine_type + ".")
        
    def open_restaurant(self):
        print("The restaurant is open.")
