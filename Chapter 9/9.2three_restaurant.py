
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print("Restanrant name is: " + self.restaurant_name + ".")
        print("Cuisine type is: " + self.cuisine_type + ".")
        
    def open_restaurant(self):
        print("The restaurant is open.")
        
restaurant1 = Restaurant("Big world", "chinese")
restaurant2 = Restaurant("Small world", "japanese")
restaurant3 = Restaurant("Medium world", "italian")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
