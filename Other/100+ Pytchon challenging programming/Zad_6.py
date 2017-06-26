import math

dane_we = input("Wpisz liczby oddzielone przecinkami: ")

tablica_int = [int(i) for i in dane_we.split(",")]

C, H = 50, 30

# Q = sqrt[(2*C*D)/H]

wynik = [round(math.sqrt((2*C*i)/H)) for i in tablica_int ] 

print(wynik)
