'''Write a program which can map() and filter() to make a list whose
elements are square of even number in [1,2,3,4,5,6,7,8,9,10].'''

lista = [1,2,3,4,5,6,7,8,9,10]

wynik = list(map(lambda x: x**2,filter(lambda x: x%2==0,lista)))

print("Kwadraty parzystych 1-10 to: ", wynik)

'''Write a program which can filter() to make a list whose elements are
even number between 1 and 20 (both included).'''

lista_parzystych = list(filter(lambda x: x%2==0, range(0,21)))

print("Parzyste od 1-20 to: ", lista_parzystych)


'''Write a program which can map() to make a list whose elements are
square of numbers between 1 and 20 (both included).'''

kwadraty = list(map(lambda x: x**2, range(0,21)))
print("Kwadraty wartosci od 1-20 to: ", kwadraty)
