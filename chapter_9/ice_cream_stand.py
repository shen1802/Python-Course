class Restaurant:
    """A representation of a restaurant in the real world"""

    def __init__(self, restaurant_name, cuisine_type):
        """The constructor of a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints the information regarding a restaurant"""
        print(f"The name of the restaurant is: {self.restaurant_name}")
        print(f"The type of the cuisine is: {self.cuisine_type}")

    def open_restaurant(self):
        """Prints the open message"""
        print(f" {self.restaurant_name} is open")


class IceCreamStand(Restaurant):
    """A representation of an icecream stand"""

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["lemon", "coconut", "strawberry", "pistachio"]

    def list_flavors(self):
        """Method that prints all the flavors available in the ice cream stand"""
        [print(flavor) for flavor in self.flavors]


restaurant = IceCreamStand("Ice", "dessert")
restaurant.list_flavors()
