"""
Modulus plugin: Provides a function to compute x modulo y.
"""

from calculator.calculation import OperationRecord
from calculator.history.history import OperationHistory
from decimal import Decimal

def mod_numbers(x: Decimal, y: Decimal) -> Decimal:
    """Return x % y and record in history."""
    record = OperationRecord.create(x, y, lambda a, b: a % b)
    OperationHistory.add_record(record)
    return record.execute()
