__author__ = 'bocian'

'''
The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square
of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def sum_square_difference(number):

    squares_of_numbers = sum([x**2 for x in range(0,number+1)])

    square_of_sum = pow(sum(range(1,number+1)),2)

    difference = square_of_sum-squares_of_numbers

    return difference





