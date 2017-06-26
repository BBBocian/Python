'''Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.'''
def sort_alfabet(wejscie):
    tablica = [x for x in wejscie.split(",")]
    tablica = sorted(tablica)
    return tablica
        
x = input("Podaj wyrazy do sortowania oddzielone przecinkiem")

print(','.join((sort_alfabet(x))))

