class Person(object):
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.konto = 0

    def wys_imie(self):
        print(self.name)

    def wys_wiek(self):
        print(self.age)

    def wplata(self,wartosc):
        self.konto+=(wartosc)

    def wyplata(self,wartosc):
        self.konto-=(wartosc)

        
ala=Person("Ala",20)
