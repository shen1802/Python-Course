class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restaurant is: {self.restaurant_name}")
        print(f"The type of the cuisine is: {self.cuisine_type}")

    def open_restaurant(self):
        print(f" {self.restaurant_name} is open")


restaurant1 = Restaurant("Maison", "French")
restaurant2 = Restaurant("Leone", "Italian")
restaurant3 = Restaurant("Donner", "Turkish")

restaurant1.open_restaurant()
restaurant2.open_restaurant()
restaurant3.open_restaurant()

