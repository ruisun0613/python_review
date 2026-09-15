"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
"""
def odd_sum(n):
    sum_number = 0

    for i in range(1,n):
        if i % 2 == 0:
            continue
        else:
            square = i ** 2
            sum_number += square
    return sum_number

print(odd_sum(9))