import random

def randomness():
    return(random.randint(1, 6))

def average():
    n = input("Enter a number of dice to throw: ")
    n1 = int(n)
    sum = 0
    print("\n")
    for i in range(1,n1+1):
        sum = randomness()+sum
        print("Die %d: %d" %(i,randomness()))
    print("\n")
    avg = sum/6
    print("Average : %.1f" %(avg))

# average()
