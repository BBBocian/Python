def print_even(inp):

    zakres = range(0,inp+1)
    lista = [x for x in zakres if x % 2 == 0]

    wynik=[]
    for i in lista:
        wynik.append(str(i))

        
    print(",".join(wynik))
