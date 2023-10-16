j = int(input("Enter a number: "))
i = 1 

for i in range(j):              # Makes the Tree Height

    n = i                       # creates an editable value equal to whatever i becomes equal to through the for loops

    for n in range(j-(n+1)):    # Prints the spaces on the left of the tree
        print(" ", end='')      # the end='' removes the new line  
        
    k = j - i                   # creates a value k that changes when the value of i changes

    for n in range((j - k)+1):  # prints the center and left of the tree by adding (j - k) + 1. The + 1 is to always create a center 
        print("*", end='')      
    
    for n in range(j - k):      # adds the right side of the tree onto the end of the last for loop 
        print("*", end='')

    print("\n")                 # creates new line

