"""
4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of
five simple foods, and store them in a tuple.
Use a for loop to print each food the restaurant offers.
Try to modify one of the items, and make sure that Python rejects the
change.
The restaurant changes its menu, replacing two of the items with different
foods. Add a line that rewrites the tuple, and then use a for loop to print
each of the items on the revised menu.
"""
menu = ("pizza", "burger", "rice", "noodles", "chicken")

# for loop print each food
for food in menu:
    print(food)

# modify one items and python will reject the change
# menu.append("sushi")

# replacing two of the items with different foods.
menu = ("salad", "sandwich", "rice", "noodles", "chicken")
for food in menu:
    print(food)