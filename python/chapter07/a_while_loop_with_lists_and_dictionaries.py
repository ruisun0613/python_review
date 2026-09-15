"""
7-8. Deli: Make a list called sandwich_orders and fill it with the names of
various sandwiches. Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list of
finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made.
"""
sandwich_orders = [
    "tuna",
    "chicken",
    "turkey",
    "pastrami",
    "ham",
]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made you {sandwich} sandwich.")

    finished_sandwiches.append(sandwich)

for finished_sandwich in finished_sandwiches:
    print(f"{finished_sandwich} was made.")

"""
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make
sure the sandwich 'pastrami' appears in the list at least three times. Add
code near the beginning of your program to print a message saying the deli
has run out of pastrami, and then use a while loop to remove all occurrences
of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.
"""
sandwich_orders = [
    "tuna",
    "chicken",
    'pastrami',
    "turkey",
    "pastrami",
    "ham",
    'pastrami'
]
finished_sandwiches = []

# remove pastrami
print("The deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print(sandwich_orders)
    
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made you {sandwich} sandwich.")

    finished_sandwiches.append(sandwich)

for finished_sandwich in finished_sandwiches:
    print(f"{finished_sandwich} was made.")
"""
7-10. Dream Vacation: Write a program that polls users about their dream
vacation. Write a prompt similar to If you could visit one place in the world,
where would you go? Include a block of code that prints the results of the
poll.
"""
question = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name: ").strip()
    response = input("\nIf you could visit one place in the world, where would you go?").strip()

    question[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ").strip()
    if repeat == 'no':
        polling_active = False

print("-------- Polling Result --------")
for name, response in question.items():
    print(f"{name} would like to visit {response}.")