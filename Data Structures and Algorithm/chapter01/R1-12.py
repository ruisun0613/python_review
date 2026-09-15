"""
Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.
"""
from random import randrange

def random_choose_fruit(my_choice):
    random_index = randrange(0, len(my_choice))
    favorite_fruit = my_choice[random_index]
    return favorite_fruit

print(random_choose_fruit(['apple', 'watermelon', 'lemon', 'banana', 'mango']))