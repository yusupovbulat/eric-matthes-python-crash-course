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

class Admin(User):
    def __init__(self, first_name, last_name, age, location, priveleges):
       super().__init__(first_name, last_name, age, location)
       self.priveleges = priveleges

    def show_priveleges(self):
        print('\nPriveleges for admin ' + self.first_name.title() + ':')
        for privelege in self.priveleges:
            print(privelege)

adm1 = Admin('bob', 'anderson', 19, 'texas', ['privelege to add message'])
adm2 = Admin('ron', 'smith', 22, 'new york', ['privelege to add message', 'privelege to delete users'])
adm3 = Admin('alice', 'idontnow', 18, 'california', ['privelege to add message', 'privelege to delete users', 'privelege to ban users'])
adm1.show_priveleges()
adm2.show_priveleges()
adm3.show_priveleges()
