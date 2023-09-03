def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a/b
    else:
        print("Cannot be divided by zero")

def calculator():

 print("Welcome to my Basic Calculator:")

while True:
    print("\n Select an operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

    choice = input("Select your choice from the above:")

    if choice in ['1', '2', '3', '4']:
        num1 = int(input("Enter your first number:"))
        num2 = int(input("Enter your second number:"))

    if choice == '1':
        result = add(num1, num2)
        print(f"Result: {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"Result: {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"Result: {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"Result: {result}")
    elif choice == '5':
        print("Goodbye")
        break

    else:
        print("Invalid entry, Try again!")


calculator()
