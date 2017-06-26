__author__ = 'bocian'

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

x = 1
k = False
while k == False:
    count = 0
    for i in range(1,21):
        if x%i == 0:
            count += 1

            if count == 20:
                print(x)
                k = True

        else:
            print(x)
            x += 1
            break

