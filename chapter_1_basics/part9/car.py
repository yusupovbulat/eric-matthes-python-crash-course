"""Class for conception of car"""
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

    def update_odometer(self, mileage):
        """
        Sets the specified value on the odometer.
        When you try to reverse the change, the change is rejected.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Увеличение показания одометра с заданным приращением"""
        self.odometer_reading += miles

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
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = 'This car can go approximately ' + str(range)
        message += ' miles on a full charge.'
        print(message)

class ElectricCar(Car):
    """Specific aspects for electric cars"""
    def __init__(self, make, model, year):
        """Initialization atribute from superclass.
        Then initializate specific atribute for electic cars"""
        super().__init__(make, model, year)
        self.battery_size = Battery()

