#prompt user for a number
number =int(input("Enter a number to see its multiplication table"))

#generate and print the multiplication table
for X in range(1, 11):
  print(X)
for Y in range(1, 11):
  print(number, "x", Y, "=", number * Y)
  #X *Y = Z