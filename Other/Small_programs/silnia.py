__author__ = 'bocian'

def silnia(x):

    if x in range(0,1):

        return 1

    return x*silnia(x-1)


def silnia2(n):
    if n<2:
        return 1
    else:
        for i in range(2,n):
            print("n=",n,"i=",i)
            n*=i
            print(n)
        return n

def pesel(x):
    if len(x)==11:
        for i in range(0,len(x)):
            if x[i].isdigit():
                print("OK")


