class Car():
    """Simple car model"""
    def __init__(self, make, model, year):
        """Initialization car params"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return formatted car specificaion"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

class Battery():
    """Simple model battery for electic car"""
    def __init__(self, battery_size=70):
        """Initialization battery attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Show information about battery power"""
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')

    def get_range(self):
        """Show range for battery"""
        if self.battery_size == 70:
            ranges = 240
        elif self.battery_size == 85:
            ranges = 270

        message = 'This car can go approximately ' + str(ranges)
        message += ' miles on a full charge.'
        print(message)
    
    def upgrade_battery(self):
        """Check battery power and set battery size if power not equals"""
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar(Car):
    """Specific characterictic for electric car"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
