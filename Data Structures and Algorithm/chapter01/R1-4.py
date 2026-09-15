"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""
def positive_integer(n):
    sum_number = 0

    for i in range(1,n):
        square = i ** 2
        sum_number += square

    return sum_number

print(positive_integer(9))