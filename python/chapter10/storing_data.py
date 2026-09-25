"""
10-11. Favorite Number: Write a program that prompts for the user’s
favorite number. Use json.dumps() to store this number in a file. Write a
separate program that reads in this value and prints the message “I know
your favorite number! It’s _____.”
"""
from pathlib import Path
import json
# Write
number = int(input("Please enter a number: "))
path = Path("python/chapter10/number.json")
f_number = json.dumps(number)
path.write_text(f_number)

# Read
content = path.read_text()
favorite_number = json.loads(content)
print(f"I know your favorite number! It’s {favorite_number}")

"""
10-12. Favorite Number Remembered: Combine the two programs you
wrote in Exercise 10-11 into one file. If the number is already stored, report
the favorite number to the user. If not, prompt for the user’s favorite number
and store it in a file. Run the program twice to see that it works.
"""
path = Path("python/chapter10/favorite_number.json")

try:
    content = path.read_text()
    favorite_number = json.loads(content)
    print(f"I know your favorite number! It’s {favorite_number}")
except FileNotFoundError:
    print("Can you tell me the number again: ")
    number = int(input())
    favorite_number = json.dumps(number)
    path.write_text(favorite_number)

"""
10-13. User Dictionary: The remember_me.py example only stores one
piece of information, the username. Expand this example by asking for two
more pieces of information about the user, then store all the information you
collect in a dictionary. Write this dictionary to a file using json.dumps(), and
read it back in using json.loads(). Print a summary showing exactly what
your program remembers about the user.
"""
from pathlib import Path
import json

path = Path('user_info.json')
if path.exists():
    contents = path.read_text()
    user_info = json.loads(contents)
    print(f"Welcome back, {user_info}!")
else:
    username = input("What is your name? ")
    age = int(input("What is your age?"))
    city = input("Where are you living in")

    user_info = {
        "user name" : username,
        "age" : age,
        "city" : city
    }

    contents = json.dumps(user_info)
    path.write_text(contents)
    print(f"We'll remember your information when you come back, {user_info}!")