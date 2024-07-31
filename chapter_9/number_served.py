class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The name of the restaurant is: {self.restaurant_name}")
        print(f"The type of the cuisine is: {self.cuisine_type}")

    def open_restaurant(self):
        print(f" {self.restaurant_name} is open")

    def set_number_served(self, new_number):
        self.number_served = new_number

    def increment_number_served(self, number):
        self.number_served += number


restaurant = Restaurant("Maison", "French")
restaurant.set_number_served(15)
restaurant.increment_number_served(4)
print(f"Total tables served: {restaurant.number_served}")

