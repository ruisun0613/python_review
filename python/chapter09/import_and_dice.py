"""
9-10. Imported Restaurant: Using your latest Restaurant class, store it in a
module. Make a separate file that imports Restaurant. Make a Restaurant
instance, and call one of Restaurant’s methods to show that the import
statement is working properly.
"""
from Inheritance import Restaurant, IceCreamStand

restaurant = Restaurant("Haidilao","Chinese")
restaurant.describe_restaurant()
restaurant.open_restaurant()

ice_cream = IceCreamStand("Freeze World", "English")
ice_cream.print_flavors()
ice_cream.describe_restaurant()
"""
9-13. Dice: Make a class Die with one attribute called sides, which has a
default value of 6. Write a method called roll_die() that prints a random
number between 1 and the number of sides the die has. Make a 6-sided die
and roll it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""
from random import randint
class Die:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        number = randint(1, self.sides)
        print(number)

roll_die = Die()
for i in range(10):
    roll_die.roll_die()

roll_10_die = Die(sides = 10)
for i in range(10):
    roll_10_die.roll_die()

roll_20_die = Die(sides = 20)
for i in range(10):
    roll_20_die.roll_die()