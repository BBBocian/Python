__author__ = 'bocian'
import math


def if_prime(x):
    '''Function checking if called number - x is a prime number. If x is a prime number, function return
True, if not return False. '''
    if x == 2:
        return True
    elif x == 1 or x % 2 == 0:              # There function eliminate number 1 cause it's not a prime number, and all
        return False                        # even numbers - the same reason.
    else:
        for i in range(3,int(math.sqrt(x))+1,2):    # Finding from sqrt(x) is faster and it's enough.
            if x % i == 0:
                return False
        return True

prim_data = []

count = 0
while len(prim_data) != 10001:              # While prim_data doesn't has 10001 elements..
    count +=1
    if if_prime(count)==True:               # Prime test every number
        prim_data.append(count)

print("VALUE 10001st:", prim_data[10000])
print(prim_data)

'''
def a(x):
    lista.append(x)

lista = []
count = 0
while len(lista) != 10:
    a(count)
    count+=1

print(lista)
'''


