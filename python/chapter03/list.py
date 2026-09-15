"""
3-1. Names: Store the names of a few of your friends in a list called names.
Print each person’s name by accessing each element in the list, one at a
time.
"""
friend_names = ["steven", "davis", "cliff"]

print(friend_names[0])
print(friend_names[1])
print(friend_names[2])

"""
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of
just printing each person’s name, print a message to them. The text of each
message should be the same, but each message should be personalized
with the person’s name.
"""
print(f"My friend is {friend_names[0].title()}")
print(f"My friend is {friend_names[1].title()}")
print(f"My friend is {friend_names[2].title()}")

"""
3-3. Your Own List: Think of your favorite mode of transportation, such as
a motorcycle or a car, and make a list that stores several examples. Use
your list to print a series of statements about these items, such as “I would
like to own a Honda motorcycle.”
"""
cars = ["Ford", "BMW", "Audi"]

print(f"I would like to own a {cars[1]} car.")