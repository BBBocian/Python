lista = [str(x) for x in range(1000,3001) if int(str(x)[0])%2==0 and int(str(x)[1])%2==0 and int(str(x)[2])%2==0 and int(str(x)[3])%2==0]
print(",".join(lista))
