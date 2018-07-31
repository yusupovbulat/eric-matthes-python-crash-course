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
