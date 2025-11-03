"""
Square plugin: Provides a function to square a number.
"""

from calculator.calculation import OperationRecord
from calculator.history.history import OperationHistory
from decimal import Decimal

def square_number(x: Decimal) -> Decimal:
    """Return the square of x and record in history."""
    record = OperationRecord.create(x, x, lambda a, b: a * b)
    OperationHistory.add_record(record)
    return record.execute()
