def convert(wejscie):
    suma=0
    for i in range(1,wejscie+1):
        suma += float(i/(i+1))
    return round(suma,2)
