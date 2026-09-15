"""
Give a single command that computes the sum from Exercise R-1.4, relying on Python’s comprehension syntax and the built-in sum function.
"""
n = 9
print(sum(i ** 2 for i in range(1,n)))