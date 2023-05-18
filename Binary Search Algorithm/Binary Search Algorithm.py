
L = input("Enter the lower bound") #Lower Bound defined
U = input("Enter the Higher bound") #Upper Bound defined

print("Think of a number, the computer will try to guess what you think off") #Tells user to think of a number

while True: #Always true
    Mid = (int(L)+int(U))//2 # Calculate the midpoint between the two bounds
    print("Is your number" ,Mid) #Prints the mid point and asks user if it their number
    Ans  = input("Press H for higher and L for lower and C for correct") #Asks user to input if it is higher, lower or Correct
    if Ans == "L": #If their Answer ia Lower then
        U = Mid # The upperbound is now the mid point

    elif Ans == "H": #If their Answer is Higher then
        L = Mid + 1 #The lowerrbound is now the midpoint +1


    elif Ans == "C": #If their Answer is correct then
        print("You were thinking of:",Mid) #Prints out the number
        exit() #Exits program
