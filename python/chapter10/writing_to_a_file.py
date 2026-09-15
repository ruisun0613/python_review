"""
10-4. Guest: Write a program that prompts the user for their name. When
they respond, write their name to a file called guest.txt.
10-5. Guest Book: Write a while loop that prompts users for their name.
Collect all the names that are entered, and then write these names to a file
called guest_book.txt. Make sure each entry appears on a new line in the
file.
"""

# 10-4
from pathlib import Path

# path = Path('python/chapter10/guest.txt')
# name = input("Please enter your name: ")
# path.write_text(name)

# contents = path.read_text()
# print(contents)

# 10-5
book_path = Path('python/chapter10/guest_book.txt')

all_names = []

while True:
    names = input("Please enter your name: (if you want to end this program, press q)")

    if names == 'q':
        break
    else:
        all_names.append(names)

book_path.write_text("\n".join(all_names))

contents = book_path.read_text()
print(contents)

