
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
        
restaurant = Restaurant("Big world", "chinese")
print(restaurant.number_served)

restaurant.number_served = 10
print(restaurant.number_served)

restaurant.set_number_served(125)
print(restaurant.number_served)

restaurant.increment_number_served(34)
print(restaurant.number_served)
