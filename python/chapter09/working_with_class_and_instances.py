"""
9-4. Number Served: Start with your program from Exercise 9-1 (page
162). Add an attribute called number_served with a default value of 0. Create
an instance called restaurant from this class. Print the number of customers
the restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number of
customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment the
number of customers who’ve been served. Call this method with any
number you like that could represent how many customers were served in,
say, a day of business.
"""
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name is : {self.restaurant_name}")
        print(f"Cuisine_type is : {self.cuisine_type}")

    def open_restaurant(self):
        print(f"This restaurant is open now.")

    def set_number_served(self,number):
        self.number_served = number
        print(f"Today services {number} customer.")

    def increment_number_served(self,new_number):
        self.number_served += new_number
        print(f"Today services {self.number_served} customer.")

restaurant = Restaurant("Haidilao","Chinese")
print(f"This restaurant is {restaurant.restaurant_name}, it provides {restaurant.cuisine_type} food.")
# restaurant.number_served = 100
# print(f"This restaurant is {restaurant.restaurant_name}, it provides {restaurant.cuisine_type} food. Today services {restaurant.number_served} customer.")
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(400)
restaurant.increment_number_served(200)

"""
9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 162). Write a method called
increment_login_attempts() that increments the value of login_attempts by 1.
Write another method called reset_login_attempts() that resets the value of
login_attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was
incremented properly, and then call reset_login_attempts(). Print
login_attempts again to make sure it was reset to 0.
"""
class User:
    def __init__(self, f_name, l_name, school, language, favorite_food):
        self.first_name = f_name
        self.last_name = l_name
        self.school = school
        self.language = language
        self.favorite_food = favorite_food
        self.login_attempts = 0

    def describe_user(self):
        print("------------ Information ------------")
        print(f"Name: {self.first_name} {self.last_name}\n School: {self.school}\n Language: {self.language}\n Favorite Food: {self.favorite_food}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, Nice to meet you.")

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts

# Calling the class
# 1
user_1 = User("Rui", "Sun", "Centennial college", "Mandarin", "Rice")
user_1.describe_user()
user_1.greet_user()

# 2
user_2 = User("David", "Kim", "Brown college", "Korean", "Kimchi")
user_2.describe_user()
user_2.greet_user()

# increment
print(user_1.increment_login_attempts())
print(user_1.reset_login_attempts())
user_1.login_attempts = 3
print(user_1.increment_login_attempts())
print(user_1.reset_login_attempts())