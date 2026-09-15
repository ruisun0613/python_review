# Strings
"""
2-3. Personal Message: Use a variable to represent a person’s name, and
print a message to that person. Your message should be simple, such as,
“Hello Eric, would you like to learn some Python today?”
"""
name = "Eric"
print(f"Hello {name}, would you like to learn some Python today?")

"""
2-4. Name Cases: Use a variable to represent a person’s name, and then
print that person’s name in lowercase, uppercase, and title case.
"""

person_name = "adAm"

Upper_name = person_name.upper()    # upper_name
Lower_name = person_name.lower()    # lower_name
Title_name = person_name.title()    # title_name
# In Python, it is best for variable names to start with a lowercase letter;
# only class names need to start with an uppercase letter.
print(f"Uppercase : {Upper_name}")
print(f"Lowercase : {Lower_name}")
print(f"Title case : {Title_name}")



"""
2-5. Famous Quote: Find a quote from a famous person you admire. Print
the quote and the name of its author. Your output should look something like
the following, including the quotation marks:
Albert Einstein once said, “A person who never made a mistake never tried anything new.”
"""

print("Steve Jobs: "+ "Your time is limited, so don't waste it living someone else's life.")
print("Steve Jobs: \"Your time is limited, so don't waste it living someone else's life.\"")


"""
2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the
famous person’s name using a variable called famous_person. Then compose
your message and represent it with a new variable called message. Print your
message.
"""
famous_person = "Steve Jobs"
message = famous_person + ": \"Your time is limited, so don't waste it living someone else's life.\""
print(message)

# another best method
message_best = f'{famous_person} + "Your time is limited, so don\'t waste it living someone else\'s life."'
print(message_best)

"""
2-7. Stripping Names: Use a variable to represent a person’s name, and
include some whitespace characters at the beginning and end of the name.
Make sure you use each character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip().
"""
person_name1 = "Jack "
person_name2 = " Alice"
person_name3 = " John "

print(person_name1 + "\n" + person_name2 + "\n" + person_name3)
print(person_name1.rstrip() + "\n" + person_name2.lstrip() + "\n" + person_name3.strip())

"""
2-8. File Extensions: Python has a removesuffix() method that works
exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable
called filename. Then use the removesuffix() method to display the filename
without the file extension, like some file browsers do.
"""
filename = "python_notes.txt"

print(filename.removesuffix(".txt"))
print(filename)