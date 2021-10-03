def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

def printfactorials():
    n = input("Enter a number: ")
    n1 = int(n)
    for i in range(1,n1):
        print("%d! = %d" %(i,factorial(i)))

# printfactorials()
