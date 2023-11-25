def isprime(m):
    prime = False
    for i in range(2, m):
        if m % i == 0:
            prime = True
            print(m," is not a prime")
            break
    if prime is False:
        print(m,"Its prime")

m=int(input("enter m = "))
n=int(input("enter n = "))
for i in range(m,n):
    isprime(i)
