
 
row = int(input("Enter a row number from 1-5: "))
col = int(input("Enter a column number from 1-5: "))
for i in range(1, 6):

    for f in range(1, 6):

        if i==row and f==col:

            print("1", end=" ")

        else:
            
            print("0", end=" ")
            
print()

