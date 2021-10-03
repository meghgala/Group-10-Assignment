#Function to create the Collatz sequence
def collatz():
    n1 = input("Enter the starting number: ")
    n = int(n1)
    print("\n")
    print("%d" %(n))
    while (n > 1):
        if(n % 2 == 0):  #If the number is divisible by 2, perform n/2
            n = n/2
            print("%d" %(n))
        else:
            n = (3*n) + 1  #If the number is not divisible by 2, perform 3n+1
            print("%d" %(n))