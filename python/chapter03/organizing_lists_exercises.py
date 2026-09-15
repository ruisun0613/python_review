"""
3-8. Seeing the World: Think of at least five places in the world you’d like to visit.

Store the locations in a list. Make sure the list is not in alphabetical order.
Print your list in its original order. Don’t worry about printing the list neatly;
just print it as a raw Python list.
Use sorted() to print your list in alphabetical order without modifying the
actual list.
Show that your list is still in its original order by printing it.
Use sorted() to print your list in reverse-alphabetical order without changing
the order of the original list.
Show that your list is still in its original order by printing it again.
Use reverse() to change the order of your list. Print the list to show that its
order has changed.
Use reverse() to change the order of your list again. Print the list to show it’s
back to its original order.
Use sort() to change your list so it’s stored in alphabetical order. Print the
list to show that its order has been changed.
Use sort() to change your list so it’s stored in reverse-alphabetical order.
Print the list to show that its order has changed.
"""

locations = ["Paris", "London", "New York", "Beijing", "Tokyo"]
print(sorted(locations))

print(sorted(locations, reverse = True))
print(locations)

locations.reverse()
print(locations)

# new_locations = locations.reverse()
# print(new_locations)

locations.reverse()
print(locations)

locations.sort()
print(locations)

locations.sort(reverse = True)
print(locations)

"""
3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
through 3-7 (pages 41–42), use len() to print a message indicating the
number of people you’re inviting to dinner.
"""
# 3.4
friend_names = ["steven", "davis", "cliff"]

print(f"Hello {friend_names[0]}, I want invite you to have a dinner.")
print(f"Hello {friend_names[1]}, I want invite you to have a dinner.")
print(f"Hello {friend_names[2]}, I want invite you to have a dinner.")

print(f"I am inviting {len(friend_names)} people to dinner.")

"""
3-10. Every Function: Think of things you could store in a list. For
example, you could make a list of mountains, rivers, countries, cities,
languages, or anything else you’d like. Write a program that creates a list
containing these items and then uses each function introduced in this
chapter at least once.
"""

# Languages
languages = ["Mandarin", "English", "French", "Japanese"]

# print
print(f"I can speak {languages[0]}")
print(f"\nI can speak {languages[1]}")
print(f"\nI can speak {languages[2].title()}")

# insert, append
languages.insert(1, "Italian")
print("\n",languages)

languages.append("Latin")
print("\n",languages)

# pop, del，remove
removed_language = languages.pop(2)
print("\n",removed_language)

another_removed_language = languages.remove("Latin")
print(another_removed_language)
print(languages)

del languages[1]
print("\n",languages)

# sort, sorted, reverse

languages.sort()
print("\n",languages)

languages.reverse()
print("\n",languages)

print(sorted(languages, reverse=True))
print(len(languages))