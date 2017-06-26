__author__ = 'bocian'

def if_prime(x):

    if x == 2:
        return True
    elif x == 1 or x % 2 == 0:
        return False
    else:
        for i in range(3,x,2):
            if x % i == 0:
                return False
        return True


def check(x):
    if x == True:
        print("TAK")
    else:
        print("NIE")

tab = []
print("Input:")
count = int(input())
if count in range(1,10000):

    for i in range(0,count):
        tab.append(int(input()))

    print("Output:")

    for i in range(0,len(tab)):
        check(tab[i])

