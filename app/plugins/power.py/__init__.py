# app/plugins/power.py
"""Command module for power operation."""

from decimal import Decimal, InvalidOperation
from app.commands import Command
from calculator.imports import CalcEngine  # adjust import path if needed

class PowerCommand(Command):
    """Command class for raising one number to the power of another."""

    def execute(self, a_str: str, b_str: str) -> None:
        """Execute power command with two numeric arguments."""
        try:
            val_a = Decimal(a_str)
            val_b = Decimal(b_str)
        except InvalidOperation:
            print(f"Invalid input: {a_str} or {b_str} is not a valid number.")
            return

        result = CalcEngine.power(val_a, val_b)
        print(f"The result of {a_str} ** {b_str} is {result}")
