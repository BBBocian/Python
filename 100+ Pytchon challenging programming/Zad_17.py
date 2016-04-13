'''Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
¡­
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500'''

acc = 0
dane = []
while True:
    wejscie = input()
    if wejscie:
        dane.append(wejscie)
    if not wejscie:
        break

for i in dane:
    linia = i
    if linia[0] == "D":
        acc+=int((linia.split(" "))[1])
    elif linia[0] == "W":
        acc-=int((linia.split(" "))[1])

print(acc)
