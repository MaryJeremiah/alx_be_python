def perform_operation(num1, num2, operation):
  if operation == 'add':
    result = num1 + num2
  elif operation == 'subtract':
    result = num1 - num2
  elif operation == 'multiply':
    result = num1 * num2
  elif operation == 'divide':
    if num2 == 0:
      print ("can not divide by zero")
      result = num1 / num2
  else:print("not a valid input")
  return result