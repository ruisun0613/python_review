"""
6-1. Person: Use a dictionary to store information about a person you
know. Store their first name, last name, age, and the city in which they live.
You should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.
"""
person = {'first_name' : 'Rui',
          'last_name' : 'Sun',
          'age': 26,
          'city' : 'Fort Mcmurray'}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])
"""
6-2. Favorite Numbers: Use a dictionary to store people’s favorite
numbers. Think of five names, and use them as keys in your dictionary.
Think of a favorite number for each person, and store each as a value in
your dictionary. Print each person’s name and their favorite number. For
even more fun, poll a few friends and get some actual data for your
program.
"""
numbers = {'Alex' : 45, 
           'James' : 39, 
           'David' : 56, 
           'Kane' : 82, 
           'Jack' : 14
           }
for name, favorite_number in numbers.items():
    print(name, favorite_number)

# another method    -- nesting
people_1 = {"name" : "Alex", "number": 45}
people_2 = {"name" : "James", "number": 39}
people_3 = {"name" : "David", "number": 56}
people_4 = {"name" : "Kane", "number": 82}
people_5 = {"name" : "Jack", "number": 14}

people = [people_1, people_2, people_3, people_4, people_5]

for person in people:
    print(person)
"""
6-3. Glossary: A Python dictionary can be used to model an actual
dictionary. However, to avoid confusion, let’s call it a glossary.
Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
Print each word and its meaning as neatly formatted output. You might print
the word followed by a colon and then its meaning, or print the word on one
line and then print its meaning indented on a second line. Use the newline
character (\n) to insert a blank line between each word-meaning pair in your
output.
"""
glossary = {
    "variable" : "A name used to store a value in a program.",
    "loop" : "A way to repeat a block of code multiple times.",
    "dictionary" : "A collection that stores data in key-value pairs.",
    "function" : "A reusable block of code designed to perform a specific task.",
    "conditional" : "A statement that runs different code depending on whether a condition is true or false."
}

for word, meaning in glossary.items():
    #print(word + ":" + "\n" + meaning + "\n")
    print(f"{word}:\n{meaning}\n")