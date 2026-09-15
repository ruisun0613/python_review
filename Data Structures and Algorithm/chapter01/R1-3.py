"""
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
"""
def minmax(data):
    smallest = data[0]
    largest = data[0]

    for number in data:
        if number < smallest:
            smallest = number 

        if number > largest:
            largest = number

    return (smallest,largest)
print(minmax([12,3,4,6,7,8]))