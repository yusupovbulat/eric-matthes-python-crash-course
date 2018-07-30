class Restaurant():
    """Simple restaurant model"""
    def __init__(self, rastaurant_name, cuisine_type):
        self.name = rastaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print('The name of this restaurant ' + self.name.title() + ' and here prepare ' + self.cuisine.title() + ' cuisine.')

    def open_restaurant(self):
        print('Restaurant ' + self.name.title() + ' is open.')

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def print_flavors(self):
        print(self.flavors)


icecream = IceCreamStand('test', 'ice cream', 'chocolate')
icecream.print_flavors()
