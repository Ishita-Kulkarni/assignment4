# app/calculation/calculation_factory.py
"""
Calculation factory with a backwards-compatible API.

Exposes:
- CalculationFactory.get_calculation(op_name)
- get_operation(op_name)         (function API expected by older tests)
- get_calculation(op_name)       (alias)
"""

# Try to import from the canonical operations package. If that fails, use the
# alternate folder name. The fallback branch is intentionally excluded from
# coverage because CI/test environments standardize on app/operations.
try:
    from app.operations.operations import OPERATION_MAP
except Exception:  # pragma: no cover
    from app.operation.operations import OPERATION_MAP  # pragma: no cover

from typing import Callable

Operation = Callable[..., float]


class CalculationFactory:
    @staticmethod
    def get_calculation(op_name: str) -> Operation:
        """
        Return a callable for the given operation name or symbol.
        Raises KeyError if operation not found.
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