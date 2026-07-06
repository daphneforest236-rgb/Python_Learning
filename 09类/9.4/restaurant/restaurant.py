#restaurant类
class restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def discribe_restaurant(self):
        print(f"Restaurant name is {self.restaurant_name.title()}.")
        print(f"Cuisine type is {self.cuisine_type}.")
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open.")
