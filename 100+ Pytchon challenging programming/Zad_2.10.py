def suma(war1,war2):
    '''function that can receive two integral numbers in string form and compute their sum and then print it in console.'''
    
    print((int(war1)+int(war2)))

#suma("5","3")

def add_str(str1,str2):
    '''function that can accept two strings as input and concatenate them and then print it in console.'''
    
    print(str(str1)+str(str2))

#add_str("ala"," ma")

def longest_str(str1,str2):
    '''Function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.'''
    
    if len(str1)==len(str2):
        print(str1,"\n"+str2)
    elif len(str1)>len(str2):
        print(str1)
    else:
        print(str2)

#longest_str("Ala","Nie")

def jaka_liczba(x):
    '''Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".'''
    
    if x%2 == 0:
        print(x,"is a even number")
    else:
        print(x,"is a odd number")
    
#jaka_liczba(9)

def druk_slownik1():
    '''Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.'''

    
    slownik = {x: x**2 for x in range(1,4)}

    for item,value in slownik.items():
        print(item,value)

def druk_slownik3():
    slownik = {x: x**2 for x in range(1,21)}

    print(slownik.values())


def print_list():
    lista = [x**2 for x in range(1,21)]
    print(lista)

def print_list2():
    '''Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.'''
    
    lista = [x**2 for x in range(1,21)]
    print(lista[:5])

def print_tup():
    lista=[x**2 for x in range(0,21)]
    tupla=tuple(lista)
    print(tupla)


def print_tup2():
    '''With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. '''
    
    tupla=(1,2,3,4,5,6,7,8,9,10)

    for i in range(0,int(len(tupla)/2)):
        print(tupla[i], end=",")

    print()

    for i in range(int(len(tupla)/2),len(tupla)):
        print(tupla[i], end=",")

def print_tup3():
    tupla=(1,2,3,4,5,6,7,8,9,10)

    lista = []
    for i in tupla:
        if i % 2 == 0:
            lista.append(i)

    lista = tuple(lista)

    print(lista)
















