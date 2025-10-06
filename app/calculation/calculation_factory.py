# app/calculation/calculation_factory.py

from app.operations.operations import OPERATION_MAP

class CalculationFactory:
    @staticmethod
    def get_calculation(op_name):
        func = OPERATION_MAP.get(op_name.lower())
        if func is None:
            raise ValueError(f"Operation '{op_name}' not supported.")
        return func
