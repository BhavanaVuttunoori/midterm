# app/plugins/modulus.py
"""Command module for modulus operation."""

from decimal import Decimal, InvalidOperation
from app.commands import Command
from calculator.imports import CalcEngine  # adjust import path if needed

class ModulusCommand(Command):
    """Command class for modulus operation."""

    def execute(self, a_str: str, b_str: str) -> None:
        """Execute modulus command with two numeric arguments."""
        try:
            val_a = Decimal(a_str)
            val_b = Decimal(b_str)
        except InvalidOperation:
            print(f"Invalid input: {a_str} or {b_str} is not a valid number.")
            return

        result = CalcEngine.modulus(val_a, val_b)
        print(f"The result of {a_str} % {b_str} is {result}")
