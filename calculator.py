# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Error: Division by zero!")
    return a / b

def calculate(choice, num1, num2):
    if choice == "1":
        return add(num1, num2)
    elif choice == "2":
        return subtract(num1, num2)
    elif choice == "3":
        return multiply(num1, num2)
    elif choice == "4":
        return divide(num1, num2)
    else:
        raise ValueError("Invalid choice!")
