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
       self.priveleges = Priveleges(priveleges)

    def admin_info(self):
        print('Admin: ' + self.first_name.title() + ' ' + self.last_name.title())
        print('Age: ' + str(self.age))
        print('Location: ' + self.location.title())
        print('Priveleges: ' + str(self.priveleges))

class Priveleges():
    def __init__(self, priveleges):
        self.priveleges = priveleges

    def show_priveleges(self):
        for privelege in self.priveleges:
            print(privelege)

adm1 = Admin('bob', 'anderson', 19, 'texas', ['privelege to add message'])
adm2 = Admin('ron', 'smith', 22, 'new york', ['privelege to add message', 'privelege to delete users'])
adm3 = Admin('alice', 'idontnow', 18, 'california', ['privelege to add message', 'privelege to delete users', 'privelege to ban users'])
adm1.admin_info()
adm2.admin_info()
adm3.admin_info()
