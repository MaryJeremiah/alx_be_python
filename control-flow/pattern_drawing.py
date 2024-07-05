
# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks in each column of the current row
    for col in range(size):
        print("*", end="")
    # Print a newline character to move to the next row
    print()
    # Move to the next row
    row += 1