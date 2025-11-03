# app/plugins/square.py
"""Command module for squaring a number."""

from decimal import Decimal, InvalidOperation
from app.commands import Command
from calculator.imports import CalcEngine  # if your CalcEngine is in calculator/imports.py
# If it's in calculator/operations.py, import from there instead:
# from calculator.operations import CalcEngine

class SquareCommand(Command):
    """Command class for squaring a number."""

    def execute(self, a_str: str) -> None:
        """Execute square command with one numeric argument."""
        try:
            val_a = Decimal(a_str)
        except InvalidOperation:
            print(f"Invalid number input: {a_str} is not a valid number.")
            return

        result = CalcEngine.square(val_a)
        print(f"The square of {a_str} is {result}")
