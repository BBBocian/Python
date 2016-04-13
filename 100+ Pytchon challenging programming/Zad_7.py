'''Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.'''

def matrix(a,b):
    x = [[i*j for i in range(0,b)] for j in range(0,a)]
    print(x)

x=[]

wejscie = input("Podaj dwie wartosci oddzielone przecinkiem: ")

wartosci = [int(i) for i in wejscie.split(",")]

kol = wartosci[0]
wiersz = wartosci[1]

matrix(kol,wiersz)
