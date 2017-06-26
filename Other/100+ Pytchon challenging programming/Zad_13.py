def lett_and_dig_counter(wejscie):

    lett_counter = 0
    dig_counter = 0

    for i in wejscie:
        if i.isdigit() == True:
            dig_counter+=1
        if i.isalpha() == True:
            lett_counter+=1

    return(print("LETTERS: {0} \nDIGITS: {1}".format(lett_counter,dig_counter)))

            


x = input("Wpisz wejscie: ")
lett_and_dig_counter(x)

'''Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
    '''
