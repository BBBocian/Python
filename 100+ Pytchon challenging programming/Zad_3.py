def wypelnij_slownik(n):
    '''Question: With a given integral number n, write a program to generate a dictionary
    that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary. Suppose the following input is supplied to the program:
    '''
    for i in range(0,n):
        dict[i]=i*i

n = int(input("Podaj liczbe: "))
dict = {}

wypelnij_slownik(n)

print(dict)
