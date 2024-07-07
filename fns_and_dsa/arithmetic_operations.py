def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
    result = 'perform_operations'(num1, num2, operation)
    print(f"Result: {result}")
