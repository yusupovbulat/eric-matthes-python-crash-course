class Restaurant():
    """Simple restaurant model"""
    def __init__(self, rastaurant_name, cuisine_type):
        self.name = rastaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print('The name of this restaurant ' + self.name.title() + ' and here prepare ' + self.cuisine.title() + ' cuisine.')

    def open_restaurant(self):
        print('Restaurant ' + self.name.title() + ' is open.')

restaurant1 = Restaurant('Raisins', 'Asian')
restaurant2 = Restaurant('ChinaTown', 'Chineese')
restaurant3 = Restaurant('Syrian shaurma', 'Syrian')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
