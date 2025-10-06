# app/operation/operations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

# Dictionary for factory
OPERATION_MAP = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}
