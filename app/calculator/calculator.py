# app/calculator/calculator.py
"""
Calculator module.

Exports:
- Calculator (class): programmatic calculator with calculate(symbol, a, b)
- calculator (instance): a module-level Calculator() instance for convenience
- calculator_repl and helper functions for CLI use (excluded from coverage)
"""

from ..calculation.calculation_factory import CalculationFactory
from ..operations.operations import OPERATION_MAP
from typing import Union

Number = Union[int, float]

class Calculator:
    """
    Simple calculator wrapper around the CalculationFactory.

    Usage:
        calc = Calculator()
        result = calc.calculate('+', 1, 2)
    """
    def __init__(self) -> None:
        self.history: list[str] = []

    def calculate(self, symbol: str, a: Number, b: Number) -> Number:
        """
        Calculate `a (symbol) b` using the factory to fetch the operation.
        Accepts both word-keys (e.g., 'add') and symbol-keys (e.g., '+').
        Raises KeyError for unknown operation and ZeroDivisionError for division by zero.
        """
        # Normalise argument (strings only)
        key = symbol if not isinstance(symbol, str) else symbol
        func = CalculationFactory.get_calculation(key)
        result = func(a, b)
        self.history.append(f"{symbol} {a} {b} = {result}")
        return result

# module-level instance for convenience (tests sometimes import `calculator`)
calculator = Calculator()

# ----------------- CLI / helpers (interactive) -----------------
# Exclude the interactive parts from coverage since they require stdin/stdout.
def print_help():  # pragma: no cover
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

def get_numbers_lbyl(input_list):  # pragma: no cover
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

def get_numbers_eafp(input_list):  # pragma: no cover
    """Easier to Ask Forgiveness than Permission"""
    try:
        a, b = float(input_list[0]), float(input_list[1])
        return a, b
    except (ValueError, IndexError):
        return None, None

def calculator_repl():  # pragma: no cover
    """Interactive REPL"""
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
            if not calculator.history:
                print("No calculations yet.")
            else:
                for i, record in enumerate(calculator.history, 1):
                    print(f"{i}: {record}")
        else:
            a, b = get_numbers_lbyl(parts[1:])  # or get_numbers_eafp(parts[1:])
            if a is None or b is None:
                continue

            try:
                result = calculator.calculate(command, a, b)
                print(f"Result: {result}")
            except KeyError as ke:
                print(ke)
            except ZeroDivisionError as zde:
                print(zde)
            except Exception as e:
                print(f"Unexpected error: {e}")

if __name__ == "__main__":  # pragma: no cover
    calculator_repl()

__all__ = ["Calculator", "calculator", "calculator_repl", "get_numbers_lbyl", "get_numbers_eafp", "print_help"]