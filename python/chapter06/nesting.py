"""
6-7. People: Start with the program you wrote for Exercise 6-1 (page 98).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.
"""
person_1 = {
    'first_name' : 'Rui',
    'last_name' : 'Sun',
    'age': 26,
    'city' : 'Fort Mcmurray'
}

person_2 = {
    'first_name' : 'David',
    'last_name' : 'Alex',
    'age': 31,
    'city' : 'Calgary'
}

person_3 = {
    'first_name' : 'John',
    'last_name' : 'Kim',
    'age': 19,
    'city' : 'Toronto'
}

people = [person_1, person_2, person_3]

for person in people:
    print(person)
"""
6-8. Pets: Make several dictionaries, where each dictionary represents a
different pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets. Next, loop through your
list and as you do, print everything you know about each pet.
"""
pets_1 = {"animal" : "cat", "owner's name" : "peter"}
pets_2 = {"animal" : "dog", "owner's name" : "kevin"}
pets_3 = {"animal" : "hamster", "owner's name" : "bob"}
pets_4 = {"animal" : "rabbit", "owner's name" : "lee"}

pets = [pets_1, pets_2, pets_3, pets_4]

for pet in pets:
    print(pet)
"""
6-9. Favorite Places: Make a dictionary called favorite_places. Think of
three names to use as keys in the dictionary, and store one to three favorite
places for each person. To make this exercise a bit more interesting, ask
some friends to name a few of their favorite places. Loop through the
dictionary, and print each person’s name and their favorite places.
"""
favorite_places = {
    "John" : ["London", "Toronto", "Tokyo"],
    "Alex" : ["Washington", "Calgary", "Paris"],
    "David" : ["Vancouver", "Beijing"],
}

for people, place in favorite_places.items():
    print(f"{people}'s favortie places are:")
    for city in place:
        print(city)
"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page
98) so each person can have more than one favorite number. Then print
each person’s name along with their favorite numbers.
"""
numbers = {'Alex' : [45, 66, 56],
           'James' : [39, 89, 31], 
           'David' : [56, 73, 43],
           'Kane' : [82, 24], 
           'Jack' : [14, 47]
           }
for name, favorite_numbers in numbers.items():
    print(f"{name}'s favorite numbers are :")
    for number in favorite_numbers:
        print(number)
"""
6-11. Cities: Make a dictionary called cities. Use the names of three cities
as keys in your dictionary. Create a dictionary of information about each city
and include the country that the city is in, its approximate population, and
one fact about that city. The keys for each city’s dictionary should be
something like country, population, and fact. Print the name of each city and
all of the information you have stored about it.
"""
cities = {
    "Calgary" : {
        "country" : "Canada",
        "population" : 1_500_000,
        "fact" : "Famous for the Calgary Stampede",
    },
    "Tokyo" : {
        "country" : "Japan",
        "population" : 14_300_300,
        "fact" : "Tokyo is the capital of Japan.",
    },
    "Shanghai": {
        "country" : "China",
        "population" : 24_850_000,
        "fact" : "Shanghai is located at the estuary of the Yangtze River.",
    },
}

for city, city_information in cities.items():
    print(city)
    print(f"\nCountry : {city_information['country']}")
    print(f"\nPopulation : {city_information['population']}")
    print(f"\nFact : {city_information['fact']}")
"""
6-12. Extensions: We’re now working with examples that are complex
enough that they can be extended in any number of ways. Use one of the
example programs from this chapter, and extend it by adding new keys and
values, changing the context of the program, or improving the formatting of
the output.
"""
cities = {
    "Calgary" : {
        "country" : "Canada",
        "population" : 1_500_000,
        "fact" : "Famous for the Calgary Stampede",
        "language" : "English"
    },
    "Tokyo" : {
        "country" : "Japan",
        "population" : 14_300_300,
        "fact" : "Tokyo is the capital of Japan.",
        "language" : "Japanese"
    },
    "Shanghai": {
        "country" : "China",
        "population" : 24_850_000,
        "fact" : "Shanghai is located at the estuary of the Yangtze River.",
        "language" : "Mandarin"
    },
}

for city, city_information in cities.items():
    print(city)
    print(f"\nCountry : {city_information['country']}")
    print(f"\nPopulation : {city_information['population']}")
    print(f"\nFact : {city_information['fact']}")
    print(f"\nLanguage : {city_information['language']}")
