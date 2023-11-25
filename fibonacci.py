a=0
b=1
n=10
def fib(a,b):
    for i in range(n):
        print(a)
        c=a+b
        a=b
        b=c

fib(a,b)
