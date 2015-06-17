def print_div_5_7(n):
    '''print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.'''

    lista = [x for x in range(0,int(n)+1) if x%5==0 and x%7==0]

    str_list = [str(x) for x in lista]

    return(print(",".join(str_list)))


n = input("value: ")

print_div_5_7(n)
