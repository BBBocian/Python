__author__ = 'bocian'
import math

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def sieve_of_eratosthenes(value):
    '''Simple sieve of eratosthenes'''

    section = list(range(2,int(value)+1))

    for prime in section:
        for multiple in range(2*prime,len(section)+1,prime):
            if multiple in section:
                section.remove(multiple)

    return section

def largest_prime_factor(number):
    '''This function is returning a prime factors of selected number'''
    i = 0                                                               # counter to count index of prime_numbers
    while number % prime_numbers[i] != 0:                               # loop is working as long as she finds first
        i+=1                                                            # prime factor

    print(prime_numbers[i])                                             # when loop finds first prime factor, hes printed

    if number/prime_numbers[i]>1:                                       # when function finds firs prime factor, main
        largest_prime_factor(number/prime_numbers[i])                   # number is divided by this firs prime factor
                                                                        # and function by recursion is looking for a
                                                                        # next first prime factor in new number created
                                                                        # by dividing the last one / first prime factor

prime_numbers = sieve_of_eratosthenes(10000)                            # don't need to check all prime numbers from 0
largest_prime_factor(600851475143)                                      # to 600851475143, it's to much - memory err.


