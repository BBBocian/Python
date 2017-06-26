'''Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=1

with a given n input by console (n>0).'''

def rec(n):
    if n==0:
        return 0
    else:
        return rec(n-1)+100
