# tests/test_calculations.py
import pytest
from app.calculator.calculator import Calculator
from app.calculation.calculation_factory import get_operation

@pytest.fixture
def calc():
    return Calculator()

@pytest.mark.parametrize(
    "symbol,a,b,expected",
    [
        ('+', 1, 2, 3),
        ('-', 5, 3, 2),
        ('*', 3, 4, 12),
        ('/', 10, 2, 5),
        ('**', 2, 3, 8),
        ('^', 2, 4, 16),
    ],
)
def test_calculator_calculations(calc, symbol, a, b, expected):
    assert calc.calculate(symbol, a, b) == expected


def test_calculator_divide_exception(calc):
    with pytest.raises(ZeroDivisionError):
        calc.calculate('/', 1, 0)


def test_factory_unknown_op():
    with pytest.raises(KeyError):
        get_operation('unknown')
