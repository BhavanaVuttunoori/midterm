from decimal import Decimal, InvalidOperation
from app.commands import Command
from calculator.imports import CalcEngine

class PowerCommand(Command):
    def execute(self, a_str: str, b_str: str) -> None:
        try:
            base = Decimal(a_str)
            exponent = Decimal(b_str)
        except InvalidOperation:
            print(f"Invalid input: {a_str}, {b_str}")
            return

        result = CalcEngine.power(base, exponent)
        print(f"{a_str} ^ {b_str} = {result}")
