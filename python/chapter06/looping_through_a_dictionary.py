"""
6-4. Glossary 2: Now that you know how to loop through a dictionary,
clean up the code from Exercise 6-3 (page 99) by replacing your series of
print() calls with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output.
"""
glossary = {
    "variable" : "A name used to store a value in a program.",
    "loop" : "A way to repeat a block of code multiple times.",
    "dictionary" : "A collection that stores data in key-value pairs.",
    "function" : "A reusable block of code designed to perform a specific task.",
    "conditional" : "A statement that runs different code depending on whether a condition is true or false.",
    "list" : "A collection used to store multiple items in a specific order.",
    "tuple" : "An ordered collection whose values cannot be changed after it is created.",
    "set" : "A collection in which each items must be unique.",
    "key" : "A unique identifier used to access a value in a dictionary.",
    "value" : "The data associated with a key in a dictionary.",
}

for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")
"""
6-5. Rivers: Make a dictionary containing three major rivers and the
country each river runs through. One key-value pair might be 'nile': 'egypt'.
Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
Use a loop to print the name of each river included in the dictionary.
Use a loop to print the name of each country included in the dictionary.
"""
rivers = {
    "nile" : "egypt",
    "seine" : "france",
    "yellow river" : "china"
}
# key + values
for river,country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}\n")
# only keys
for river in rivers.keys():
    print(river)
print("\n")
# only values
for country in rivers.values():
    print(country)
"""
6-6. Polling: Use the code in favorite_languages.py (page 96).
Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
Loop through the list of people who should take the poll. If they have already
taken the poll, print a message thanking them for responding. If they have
not yet taken the poll, print a message inviting them to take the poll.
"""
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }

people = ["sarah", "edward", "alex", "john", "jen", "alice"]

for person in people:
    if person in favorite_languages.keys():
        print(f"Hi {person}, thank you for your responding!")
    else:
        print(f"Hi {person}, please take the poll.")