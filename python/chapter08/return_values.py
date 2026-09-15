"""
8-6. City Names: Write a function called city_country() that takes in the
name of a city and its country. The function should return a string formatted
like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the
values that are returned.
"""
def city_country(city_name, country):
    message = f"{city_name}, {country}"
    print(message)
    return message

city_country("Beijing", "China")
city_country("London", "England")
city_country(city_name="Paris", country="France")
"""
8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing
different albums. Print each return value to show that the dictionaries are
storing the album information correctly.
Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value
for the number of songs, add that value to the album’s dictionary. Make at
least one new function call that includes the number of songs on an album.
"""
def make_album(artist, album):
    person = {'artist_name': artist.title(), 'album_title': album}
    return person

print(make_album("taylor swift", "1989"))
print(make_album(artist="adele", album="21"))
print(make_album("michael jackson", "Thriller"))
"""
8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have
that information, call make_album() with the user’s input and print the
dictionary that’s created. Be sure to include a quit value in the while loop.
"""
# def make_album(artist, album):
#     person = {'artist_name': artist.title(), 'album_title': album}
#     return person

# while True:
#     print("Please enter an album’s artist and title: ")
#     print("(enter 'q' at any time to quit)")

#     if artist == 'q':
#         break
#     if album == 'q':
#         break
    
#     # active = True

#     artist = input("Please enter the artist name:")

#     album = input("Please enter the album title:")
#     print(make_album(artist, album))

def make_album(artist, album):
    person = {'artist_name': artist.title(), 'album_title': album}
    return person

active = True

while active:
    print("Please enter an album’s artist and title: ")
    print("(enter 'q' at any time to quit)")

    artist = input("Please enter the artist name:")
    if artist == 'q':
        active = False
    else:
        album = input("Please enter the album title:")

        if album == 'q':
            active = False
        else:
            print(make_album(artist, album))