from decimal import Decimal, InvalidOperation
from app.commands import Command
from calculator.imports import CalcEngine  # adjust if needed

class SquareCommand(Command):
    def execute(self, a_str: str) -> None:
        try:
            val_a = Decimal(a_str)
        except InvalidOperation:
            print(f"Invalid number input: {a_str} is not a valid number.")
            return

        result = CalcEngine.square(val_a)
        print(f"The square of {a_str} is {result}")
