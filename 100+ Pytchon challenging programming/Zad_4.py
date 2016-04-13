'''Question:
Write a program which accepts a sequence of comma-separated numbers
from console and generate a list and a tuple which contains every number.'''

dane_we = input("Wpisz liczby oddzielone przecinkami")

tablica = dane_we.split(",")

tab_int = [int(i) for i in tablica]
tup_int = tuple(tab_int)

print(tab_int,tup_int)
