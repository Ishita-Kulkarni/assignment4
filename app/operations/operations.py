# app/operation/operations.py
from typing import Union, Callable

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    return a + b

def subtract(a: Number, b: Number) -> Number:
    return a - b

def multiply(a: Number, b: Number) -> Number:
    return a * b

def divide(a: Number, b: Number) -> Number:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def power(a: Number, b: Number) -> Number:
    # support negative and fractional exponents
    return pow(a, b)

# Dictionary for factory: include both word keys and symbol keys so callers
# can use "add" or "+" (and similarly for ** and ^).
OPERATION_MAP: dict[str, Callable[..., Number]] = {
    "add": add,
    "+": add,
    "subtract": subtract,
    "-": subtract,
    "multiply": multiply,
    "*": multiply,
    "divide": divide,
    "/": divide,
    "power": power,
    "**": power,
    "^": power,
}
