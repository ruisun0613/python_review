"""
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message
indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.
"""
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name is : {self.restaurant_name}")
        print(f"Cuisine_type is : {self.cuisine_type}")

    def open_restaurant(self):
        print(f"This restaurant is open now.")

favorite_restaurant = Restaurant("Haidilao","Chinese")
print(f"This restaurant is {favorite_restaurant.restaurant_name}, it provides {favorite_restaurant.cuisine_type} food.")
favorite_restaurant.describe_restaurant()
favorite_restaurant.open_restaurant()

"""
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create
three different instances from the class, and call describe_restaurant() for
each instance.
"""
# 1
favorite_restaurant_1 = Restaurant("Haidilao","Chinese")
print(f"This restaurant is {favorite_restaurant_1.restaurant_name}, it provides {favorite_restaurant_1.cuisine_type} food.")
favorite_restaurant_1.describe_restaurant()

# 2
favorite_restaurant_2 = Restaurant("Sushi","Japanese")
print(f"This restaurant is {favorite_restaurant_2.restaurant_name}, it provides {favorite_restaurant_2.cuisine_type} food.")
favorite_restaurant_2.describe_restaurant()

# 3
favorite_restaurant_3 = Restaurant("Hello food","England")
print(f"This restaurant is {favorite_restaurant_3.restaurant_name}, it provides {favorite_restaurant_3.cuisine_type} food.")
favorite_restaurant_3.describe_restaurant()
"""
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically
stored in a user profile. Make a method called describe_user() that prints a
summary of the user’s information. Make another method called greet_user()
that prints a personalized greeting to the user.
Create several instances representing different users, and call both
methods for each user.
"""
class User:
    def __init__(self, f_name, l_name, school, language, favorite_food):
        self.first_name = f_name
        self.last_name = l_name
        self.school = school
        self.language = language
        self.favorite_food = favorite_food

    def describe_user(self):
        print("------------ Information ------------")
        print(f"Name: {self.first_name} {self.last_name}\n School: {self.school}\n Language: {self.language}\n Favorite Food: {self.favorite_food}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, Nice to meet you.")

# Calling the class
# 1
user_1 = User("Rui", "Sun", "Centennial college", "Mandarin", "Rice")
user_1.describe_user()
user_1.greet_user()

# 2
user_2 = User("David", "Kim", "Brown college", "Korean", "Kimchi")
user_2.describe_user()
user_2.greet_user()