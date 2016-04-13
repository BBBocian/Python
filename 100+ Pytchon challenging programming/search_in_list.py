def search_in_list(lista,numb):
    count = 0
    for i in lista:
        if i == numb:
            print("Value:",numb,"is on: ",count,"position")
        else:
            count+=1

lista = [0,1,2,3,4,5,6]

search_in_list(lista,4)
