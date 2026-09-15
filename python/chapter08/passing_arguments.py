"""
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should
print a sentence summarizing the size of the shirt and the message printed
on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
"""
def make_shirt(size, text):
    print(f"The shirt is size {size} and has '{text}' printed on it.")

# positional argument
make_shirt(12, "New York")
# keyword argument
make_shirt(size = 12, text = "New York")
"""
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a
different message.
"""
def make_shirt(size="large", message="I love Python"):
    print(f"The shirt is size {size} and has '{message}' printed on it.")

# large
make_shirt()
# medium
make_shirt("medium")
# small
make_shirt(size="small", message="New York")
"""
8-5. Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.
"""
def describe_city(city_name, country="Canada"):
    print(f"{city_name} is in {country}.")

describe_city("Toronto")
describe_city(city_name="Calgary")
describe_city("Tokyo", "Japan")