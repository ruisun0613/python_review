"""
7-1. Rental Car: Write a program that asks the user what kind of rental car
they would like. Print a message about that car, such as “Let me see if I can
find you a Subaru.”
"""
car = input("please choose a car brand: ")
print(f"Let me see if I can find you a {car}.")
"""
7-2. Restaurant Seating: Write a program that asks the user how many
people are in their dinner group. If the answer is more than eight, print a
message saying they’ll have to wait for a table. Otherwise, report that their
table is ready.
"""
seat = int(input("Please input how many people are in the dinner group: "))

if seat > 8 :
    print("You will have to wait for a table.")
else:
    print("Your table is ready.")
"""
7-3. Multiples of Ten: Ask the user for a number, and then report whether
the number is a multiple of 10 or not.
"""
number = int(input("Please input a number: "))

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")