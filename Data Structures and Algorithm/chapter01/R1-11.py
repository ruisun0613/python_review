"""
Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
"""

print(list(2 ** i for i in range(0,9)))
print([2 ** i for i in range(9)])