wejscie = input("Wpisz co chcesz: ")

litery = {"UPPER":0,"LOWER":0}

for i in wejscie:
    if i.islower() == True:
        litery["LOWER"]+=1
    elif i.isupper() == True:
        litery["UPPER"]+=1
    else:
        pass

print("UPPER CASE: ", litery["UPPER"])
print("LOWER CASE: ", litery["LOWER"])
        

'''Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9'''
