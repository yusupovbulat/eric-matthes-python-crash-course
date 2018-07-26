class User():

    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        """Information about user"""
        print("\nInformation about user:")
        print("- first name: " + self.first_name.title())
        print("- last name: " + self.last_name.title())
        print("- age: " + str(self.age))
        print("- location: " + self.location.title())

    def greet_user(self):
        print('Hello, ' + self.first_name.title() + ' ' + self.last_name.title() + '!')


user1 = User('bob', 'anderson', 19, 'texas')
user2 = User('ron', 'smith', 22, 'new york')
user3 = User('alice', 'idontnow', 18, 'california')
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
