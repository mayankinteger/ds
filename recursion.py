'''def rec(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return n + rec(n-1)

print(rec(5))'''

'''def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)

print(fib(4))'''

def rec(n):
    a=0
    if len(n)==1:
        return n[0]
    return n[-1] + rec(n[:-1])

print(rec([1,2,3]))