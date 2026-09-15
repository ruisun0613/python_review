"""
8-12. Sandwiches: Write a function that accepts a list of items a person
wants on a sandwich. The function should have one parameter that collects
as many items as the function call provides, and it should print a summary
of the sandwich that’s being ordered. Call the function three times, using a
different number of arguments each time.
"""
def order_sandwich(*toppings):
    print(toppings)

# 1 item
order_sandwich("tuna")

# 2 items
order_sandwich("ham", "turkey")

# 4 items
order_sandwich("tuna", "chicken", "turkey", "pastrami")
"""
8-13. User Profile: Start with a copy of user_profile.py from page 148.
Build a profile of yourself by calling build_profile(), using your first and last
names and three other key-value pairs that describe you.
"""
def build_profile(first, last, **user_info):
 """Build a dictionary containing everything we know abouta user."""
 user_info['first_name'] = first
 user_info['last_name'] = last
 return user_info
user_profile = build_profile(
   'albert', 
   'einstein', 
   location='princeton', 
   field='physics')

myself_profile = build_profile(
   'Rui',
   'Sun',
   location = 'Fort Mcmurray',
   field = 'Computer Science',
   language = 'Python'
)
print(user_profile)
print(myself_profile)
"""
8-14. Cars: Write a function that stores information about a car in a
dictionary. The function should always receive a manufacturer and a model
name. It should then accept an arbitrary number of keyword arguments. Call
the function with the required information and two other name-value pairs,
such as a color or an optional feature. Your function should work for a call
like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was
stored correctly.
"""
def make_car(manufacturer, model, **car_info):
   car_info['manufacturer'] = manufacturer
   car_info['model'] = model
   return car_info

# first car
first_car = make_car(
    'toyota',
    'rav4',
    color = 'white',
    awd = True
)

# Second car
second_car = make_car(
   'mazda',
   'cx-5',
   color = 'red',
   sunroof = True
)

# Third car
third_car = make_car(
   'volkswagen',
   'tiguan',
   color = 'black',
   heated_seat = True
)

print(first_car)
print(second_car)
print(third_car)