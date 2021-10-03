def collatz():
    n1 = input("Enter the starting number: ")
    n = int(n1)
    print("\n")
    print("%d" %(n))
    while (n > 1):
        if(n % 2 == 0):
            n = n/2
            print("%d" %(n))
        else:
            n = (3*n) + 1
            print("%d" %(n))


collatz()
