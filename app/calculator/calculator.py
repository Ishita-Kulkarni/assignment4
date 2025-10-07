# app/calculator/calculator.py

from ..calculation.calculation_factory import CalculationFactory
from ..operations.operations import OPERATION_MAP

# app/calculator/calculator.py
from ..calculation.calculation_factory import CalculationFactory

class Calculator:
    def __init__(self):
        self.history = []

    def calculate(self, command: str, a: float, b: float):
        func = CalculationFactory.get_calculation(command)
        result = func(a, b)
        self.history.append(f"{command} {a} {b} = {result}")
        return result

history = []

def print_help():
    print("""
Available commands:
  add        : Addition
  subtract   : Subtraction
  multiply   : Multiplication
  divide     : Division
  history    : Show past calculations
  help       : Show this message
  exit       : Exit the calculator
Usage:
  Enter operation followed by two numbers separated by space.
Example:
  add 5 10
""")

def get_numbers_lbyl(input_list):
    """Look Before You Leap input validation"""
    if len(input_list) != 2:
        print("Error: You must provide exactly 2 numbers.")
        return None, None
    try:
        a, b = float(input_list[0]), float(input_list[1])
        return a, b
    except ValueError:
        print("Error: Invalid number format.")
        return None, None

def get_numbers_eafp(input_list):
    """Easier to Ask Forgiveness than Permission"""
    try:
        a, b = float(input_list[0]), float(input_list[1])
        return a, b
    except (ValueError, IndexError):
        return None, None

def calculator_repl():
    print("Welcome to CLI Calculator! Type 'help' for commands.")
    while True:
        user_input = input(">> ").strip()
        if not user_input:
            continue

        parts = user_input.split()
        command = parts[0].lower()

        if command == "exit":
            print("Goodbye!")
            break
        elif command == "help":
            print_help()
        elif command == "history":
            if not history:
                print("No calculations yet.")
            else:
                for i, record in enumerate(history, 1):
                    print(f"{i}: {record}")
        else:
            # Choose input validation: LBYL or EAFP
            a, b = get_numbers_lbyl(parts[1:])  # or get_numbers_eafp(parts[1:])
            if a is None or b is None:
                continue

            try:
                func = CalculationFactory.get_calculation(command)
                result = func(a, b)
                print(f"Result: {result}")
                history.append(f"{command} {a} {b} = {result}")
            except ValueError as ve:
                print(ve)
            except ZeroDivisionError as zde:
                print(zde)
            except Exception as e:
                print(f"Unexpected error: {e}")

if __name__ == "__main__":
    calculator_repl()
