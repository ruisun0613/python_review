"""
10-6. Addition: One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to
convert the input to an int, you’ll get a ValueError. Write a program that
prompts for two numbers. Add them together and print the result. Catch the
ValueError if either input value is not a number, and print a friendly error
message. Test your program by entering two numbers and then by entering
some text instead of a number.
"""
# try:
#     a = int(input("Please enter number:")) 
#     b = int(input("Please enter another number:"))
#     result = a + b
#     print(result)
# except ValueError:
#     print("Please enter correct numerical number, not text.")
"""
10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while
loop so the user can continue entering numbers, even if they make a
mistake and enter text instead of a number.
"""
# while True:
#     try:
#         a = int(input("Please enter number:")) 
#         b = int(input("Please enter another number:"))
#         result = a + b
#         print(result)
#         break
#     except ValueError:
#         print("Please enter correct numerical number, not text.")

"""
10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least
three names of cats in the first file and three names of dogs in the second
file. Write a program that tries to read these files and print the contents of
the file to the screen. Wrap your code in a try-except block to catch the
FileNotFound error, and print a friendly message if a file is missing. Move one
of the files to a different location on your system, and make sure the code in
the except block executes properly.
"""
from pathlib import Path

# Cat
try:
    path_cat = Path('cat.txt')
    cat = path_cat.read_text()
    print(cat)
except FileNotFoundError:
    print("Check your file location.")
# Dog
try:
    path_dog = Path('dog.txt')

    dog = path_dog.read_text()

    print(dog)

except FileNotFoundError:
    print("Check your file location.")
"""
10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-7 to
fail silently if either file is missing.
"""
from pathlib import Path

# Cat
try:
    path_cat = Path('cat.txt')
    cat = path_cat.read_text()
    print(cat)
except FileNotFoundError:
    pass
# Dog
try:
    path_dog = Path('dog.txt')

    dog = path_dog.read_text()

    print(dog)

except FileNotFoundError:
    pass