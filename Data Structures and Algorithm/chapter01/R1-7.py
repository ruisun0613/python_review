"""
Give a single command that computes the sum from Exercise R-1.6, relying on Python’s comprehension syntax and the built-in sum function
"""

n = 7
print(sum(i ** 2 for i in range(1,n,2)))