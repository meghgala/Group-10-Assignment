import random

def randomness():
    return(random.randint(1, 6))

def average():
    n = input("Enter a number of dice to throw: ")    #take input from user for number of iterations
    n1 = int(n)
    sum = 0
    print("\n")
    for i in range(1,n1+1):
        sum = randomness()+sum                         #calling the random number function and calc sum of the throws
        print("Die %d: %d" %(i,randomness()))
    print("\n")
    avg = sum/6                                        # calculating average of the numbers got over different throws
    print("Average : %.1f" %(avg))

# average()
