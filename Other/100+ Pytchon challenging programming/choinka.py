def choinka(wysokosc):
    '''Podaj wysokosc choinki

    W arg podaj wysokosc choinki np. : nauka.choinka(5)'''


    spacje=wysokosc-1
    iksy=1
    for h in range(0,wysokosc+1):

            if h==wysokosc:
                for i in range(0,wysokosc-1):
                    print(" ", end="")
                print("X")
                break
            
            for i in range(0,spacje):
                print(" ", end="")
            
            for j in range(0,h+iksy):
                print("x",end="")

            for k in range(0,1):
                print("")
            spacje-=1
            iksy+=1

        
