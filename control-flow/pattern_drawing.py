#prompt the user for the size of the pattern
size =int(input("Enter the size of the pattern: "))

#Ensure the size is a  positive integer
if size <= 0:
    print("Please enter a positive integer.")

#Initialize the row
Row = 0



# Use a for loop to print asterisks in each row
for _ in range(size):
    print("*", end="")
# Move to the next line after printing each row
    print()
# Increment the row counter
    Row += 1