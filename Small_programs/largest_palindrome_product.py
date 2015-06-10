__author__ = 'bocian'

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''

def largest_palindrome_product(number):
    all_numbers = []                                                           # list for all numbers

    for x in range(0,number+1):                                                # loop adding all numbers to list
        for k in range(0,number+1):
            all_numbers.append(x*k)

    palindrome = [int(x) for x in all_numbers if str(x) == str(x)[::-1]]       # finding palindrome

    print(max(palindrome))


