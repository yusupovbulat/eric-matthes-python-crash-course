class Restaurant():
    """Simple restaurant model"""
    def __init__(self, rastaurant_name, cuisine_type):
        self.name = rastaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def increment_number_served(self, number):
        self.number_served += number

    def describe_restaurant(self):
        print('The name of this restaurant ' + self.name.title() + ' and here prepare ' + self.cuisine.title() + ' cuisine.')

    def open_restaurant(self):
        print('Restaurant ' + self.name.title() + ' is open.')

restaurant = Restaurant('Testname', 'Asian')
print('Served number = ' + str(restaurant.number_served))
restaurant.number_served = 2
print('Served number = ' + str(restaurant.number_served))
restaurant.increment_number_served(50)
print('Served number = ' + str(restaurant.number_served))
