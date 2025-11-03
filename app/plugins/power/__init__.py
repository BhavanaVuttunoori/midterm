"""
Power plugin: Provides a function to raise x to the power of y.
"""

from calculator.calculation import OperationRecord
from calculator.history.history import OperationHistory
from decimal import Decimal

def power_numbers(x: Decimal, y: Decimal) -> Decimal:
    """Return x raised to the power y and record in history."""
    record = OperationRecord.create(x, y, lambda a, b: a ** b)
    OperationHistory.add_record(record)
    return record.execute()
