# Simple Calculator Program

# Function for addition operation
def add(a, b):
    return a + b

# Function for subtraction operation
def subtract(a, b):
    return a - b

# Function for multiplication operation
def multiply(a, b):
    return a * b

# Function for division operation
def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    else:
        return a / b

# Main program loop
while True:
    # Show user all operation options
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Get user input for operation index and numbers
    operation = input("Enter operation name: ").lower()
    if operation not in ['addition', 'subtraction', 'multiplication', 'division', '1', '2', '3', '4']:
        print("Invalid operation!")
        continue
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Call the appropriate function based on the operation input by the user
    if operation == 'addition' or operation == '1':
        result = add(num1, num2)
    elif operation == 'subtraction' or operation == '2':
        result = subtract(num1, num2)
    elif operation == 'multiplication' or operation == '3':
        result = multiply(num1, num2)
    else:
        result = divide(num1, num2)

    # Print the result of the operation
    print("Result: ", result)

    # Ask if user wants to continue or not
    choice = input("Do you want to continue? (y/n)").lower()
    if choice == 'n':
        break
