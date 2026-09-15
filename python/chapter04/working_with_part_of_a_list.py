"""
4-10. Slices: Using one of the programs you wrote in this chapter, add
several lines to the end of the program that do the following:
Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.
"""
# Programming languages

languages = ["Python", "Java", "C", "C++", "JavaScript", "SQL", "R"]

# Print the first three items in the list.
print(languages[0:3])       # print(languages[:3])

# Print the middle three items in the list.
print(languages[2:5])       

# Print the last three items in the list.
print(languages[-3:])
"""
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
(page 56). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do
the following:
Add a new pizza to the original list.
Add a different pizza to the list friend_pizzas.
Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message 
My friend’s favorite pizzas are:, and then use a for loop to print the second list.
Make sure each new pizza is stored in the appropriate list.
"""
my_pizzas = ["Pepperoni", "Cheese", "Hawaiian", "Margherita"]
my_friend_pizzas = my_pizzas[0:4]

# add
my_pizzas.insert(2,"BBQ Chicken")
my_friend_pizzas.append("Meat Lovers")

print(my_pizzas)
print(my_friend_pizzas)

# for loop
print(f"My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("My friend’s favorite pizzas are")
for pizza in my_friend_pizzas:
    print(pizza)
"""
4-12. More Loops: All versions of foods.py in this section have avoided
using for loops when printing, to save space. Choose a version of foods.py,
and write two for loops to print each list of foods.
"""
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
for food in my_foods:
    print(food)
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)