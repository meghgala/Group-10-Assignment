from printingFactorials import printfactorials
from randomness import average
from collatz import collatz

while 1:
    print("This program is from group 10")
    print("Please select one of the features below, stop by entering Q.")
    print("1. Factorials\n2. Randomness\n3. Collatz")
    choice = input("Enter choice (stop with Q):")
    if(choice == "1"):
        printfactorials()
    elif(choice == "2"):
        average()
    elif(choice == "3"):
        collatz()
    elif(choice == "Q"):
        break
