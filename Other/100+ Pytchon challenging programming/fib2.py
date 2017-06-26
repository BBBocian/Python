def fib2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if n > 1:
        return fib2(n-1)+ fib2(n-2)
n = int(input())
liczby = [str(fib2(x)) for x in range(0,n+1)]
print(",".join(liczby))


