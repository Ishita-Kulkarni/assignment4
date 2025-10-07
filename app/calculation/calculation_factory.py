# app/calculation/calculation_factory.py
"""
Calculation factory with a backwards-compatible API.

Exposes:
- CalculationFactory.get_calculation(op_name)
- get_operation(op_name)         (function API expected by older tests)
- get_calculation(op_name)       (alias)
"""

# Try to import from either possible operations package name.
try:
    from app.operations.operations import OPERATION_MAP
except Exception:
    from app.operation.operations import OPERATION_MAP  # fallback

from typing import Callable

Operation = Callable[..., float]


class CalculationFactory:
    @staticmethod
    def get_calculation(op_name: str) -> Operation:
        """
        Return a callable for the given operation name or symbol.
        Raises KeyError if operation not found (matches test expectations).
        """
        key = op_name.lower() if isinstance(op_name, str) else op_name
        func = OPERATION_MAP.get(key)
        if func is None:
            # Match tests that expect KeyError for unknown op
            raise KeyError(f"Operation '{op_name}' not supported.")
        return func


# Backwards-compatible function API
def get_operation(op_name: str) -> Operation:
    return CalculationFactory.get_calculation(op_name)

# Alias
get_calculation = get_operation

__all__ = ["CalculationFactory", "get_operation", "get_calculation"]