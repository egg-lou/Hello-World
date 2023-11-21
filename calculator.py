def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"

while True:
    # Take user input for operation and numbers
    operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ")

    # Check if the user wants to exit
    if operation.lower() == 'exit':
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter valid numbers")
        continue

    # Perform the selected operation
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    else:
        print("Error: Invalid operation")
        continue

    # Display the result
    print(f"Result: {result}")
