"""
5-1. Conditional Tests: Write a series of conditional tests. Print a
statement describing each test and your prediction for the results of each
test. Your code should look something like this:
    car = 'subaru'
    print("Is car == 'subaru'? I predict True.")
    print(car == 'subaru')
    print("\nIs car == 'audi'? I predict False.")
    print(car == 'audi')
Look closely at your results, and make sure you understand why each line
evaluates to True or False.
Create at least 10 tests. Have at least 5 tests evaluate to True and another 5
tests evaluate to False.
"""
name = "Rui"
game = "Cyberpunk"
age = 26
food = "rice"
cpu = "Intel"
# 1)
print("Is name == 'Rui'? I predict True.")
print(name == "Rui")
print("Is name == 'Sun'? I predict False.")
print(name == "Sun")

# 2)
print("Is age > 26? I predict False.")
print(age > 26)
print("Is age == 26? I predict True.")
print(age == 26)

# 3)
print("Is game == 'Counter-Strike 2'? I predict False.")
print(game == "Counter-Strike 2")
print("Is game == 'Cyberpunk'?, I predict true.")
print(game == "Cyberpunk")

# 4)
print("Is food == 'rice'? I predict True.")
print(food == "rice")
print("Is food == 'sushi'? I predict False.")
print(food == "sushi")

# 5)
print("Is cpu == 'Intel'? I predict True.")
print(cpu == "Intel")
print("Is cpu == 'AMD'? I predict False.")
print(cpu == "AMD")

"""
5-2. More Conditional Tests: You don’t have to limit the number of tests
you create to 10. If you want to try more comparisons, write more tests and
add them to conditional_tests.py. Have at least one True and one False result
for each of the following:
Tests for equality and inequality with strings
Tests using the lower() method
Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
Tests using the and keyword and the or keyword
Test whether an item is in a list
Test whether an item is not in a list
"""
score = 85
car = ["audi", "bmw", "toyota"]
# 1) age 
print("Is age != 26? I predict False.")
print(age != 26)
print("Is age == 26? I predict True.")
print(age == 26)

# 2) name
print("Is lowercase of name == 'rui'? I predict True.")
print(name.lower() == "rui")
print("Is lowercase of name == 'sun'? I predict False.")
print(name.lower() == "sun")

# 3）score
print("Is score greater than 90? I predict False.")
print(score > 90)
print("Is score less than 74? I predict False.")
print(score < 74)

print("Is score great than or equal to 85? I predict True.")
print(score >= 85)
print("Is score less than or equal to 88? I predict True.")
print(score <= 88)

# 4) and / or
print("Is food == 'rice' and game == 'Cyberpunk'? I predict True.")
print(food == "rice" and game == "Cyberpunk")
print("Is name == 'Rui' and cpu == 'AMD'? I predict False.")
print(name == "Rui" and cpu == "AMD")

print("Is food == 'sushi' or game == 'Cyberpunk'? I predict True.")
print(food == "sushi" or game == "Cyberpunk")
print("Is name == 'David' or cpu == 'AMD'? I predict False.")
print(name == "David" or cpu == "AMD")

# 5) list
print("Is bmw in the list? I predict True")
print("bmw" in car)
print("Is honda in the list? I predict False.")
print("honda" in car)

print("Is audi not in the list? I predict False.")
print("audi" not in car)
print("Is mazda not in the list? I predict True.")
print("mazda" not in car)