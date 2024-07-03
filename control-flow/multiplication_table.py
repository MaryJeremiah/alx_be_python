#prompt user for a number
number =int(input("Enter a number to see its multiplication table"))

#generate and print the multiplication table
for i in range(1, 11):
  print(f"{number}*{i} ={number *i}")