"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
Write a class called IceCreamStand that inherits from the Restaurant class you
wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version
of the class will work; just pick the one you like better. Add an attribute
called flavors that stores a list of ice cream flavors. Write a method that
displays these flavors. Create an instance of IceCreamStand, and call this
method.
"""
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name is : {self.restaurant_name}")
        print(f"Cuisine_type is : {self.cuisine_type}")

    def open_restaurant(self):
        print(f"This restaurant is open now.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = [
        "Vanilla",
        "Chocolate",
        "Strawberry",
        "Mint Chocolate Chip",
        "Cookies and Cream",
        "Mango"
    ]

    def print_flavors(self):
        for flavor in self.flavors:
            print(f"We have {flavor} flavor ice cream.")

ice_cream = IceCreamStand("Freeze World", "English")
ice_cream.print_flavors()
ice_cream.describe_restaurant()
"""
9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) or
Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of
strings like "can add post", "can delete post", "can ban user", and so on. Write a
method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.
"""
class User:
    def __init__(self, f_name, l_name, school, language, favorite_food):
        self.first_name = f_name
        self.last_name = l_name
        self.school = school
        self.language = language
        self.favorite_food = favorite_food

    def describe_user(self):
        print("------------ Information ------------")
        print(f"Name: {self.first_name} {self.last_name}\n School: {self.school}\n Language: {self.language}\n Favorite Food: {self.favorite_food}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, Nice to meet you.")

class Admin(User):
    def __init__(self, f_name, l_name, school, language, favorite_food):
        super().__init__(f_name, l_name, school, language, favorite_food)
        self.privileges = [
            "can add post", "can delete post", "can ban user",
        ]

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"User {privilege}")

user = Admin("Rui", "Sun", "Centennial college", "Mandarin", "Rice")
user.describe_user()
user.greet_user()
user.show_privileges()

"""
9-8. Privileges: Write a separate Privileges class. The class should have
one attribute, privileges, that stores a list of strings as described in Exercise
9-7. Move the show_privileges() method to this class. Make a Privileges
instance as an attribute in the Admin class. Create a new instance of Admin
and use your method to show its privileges.
"""
class User:
    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

class Privileges:
    def __init__(self):
        self.privileges = [
            "can add post", "can delete post", "can ban user"
        ]

    def show_privileges(self):
            for privilege in self.privileges:
                print(f"Admin {privilege}")

class Admin(User):
    def __init__(self, f_name, l_name):
        super().__init__(f_name, l_name)
        self.previleges = Privileges()

admin = Admin("Rui", "Sun")
admin.previleges.show_privileges()

"""
9-9. Battery Upgrade: Use the final version of electric_car.py from this
section. Add a method to the Battery class called upgrade_battery(). This
method should check the battery size and set the capacity to 65 if it isn’t
already. Make an electric car with a default battery size, call get_range()
once, and then call get_range() a second time after upgrading the battery.
You should see an increase in the car’s range.
"""
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")


# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.describe_battery()
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()

my_car = ElectricCar('Tesla', 'model Y', 2025)
print(my_car.get_descriptive_name())
my_car.describe_battery()
my_car.battery.describe_battery()
my_car.battery.get_range()
my_car.battery.upgrade_battery()
my_car.battery.get_range()