from car import Car


class Battery():
    """Simple model electric car battery"""
    def __init__(self, battery_size=60):
        """Initialization battery atributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Show information about battery power."""
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')

    def get_range(self):
        """Displays approximate run reserve for the battery"""
        if self.battery_size == 70:
            ranges = 240
        elif self.battery_size == 85:
            ranges = 270

        message = 'This car can go approximately ' + str(ranges)
        message += ' miles on a full charge.'
        print(message)


class ElectricCar(Car):
    """Specific aspects for electric cars"""
    def __init__(self, make, model, year):
        """Initialization atribute from superclass.
        Then initializate specific atribute for electic cars"""
        super().__init__(make, model, year)
        self.battery = Battery()
