from decimal import Decimal, InvalidOperation
from app.commands import Command
from calculator.imports import CalcEngine

class ModulusCommand(Command):
    def execute(self, a_str: str, b_str: str) -> None:
        try:
            a = Decimal(a_str)
            b = Decimal(b_str)
        except InvalidOperation:
            print(f"Invalid input: {a_str}, {b_str}")
            return

        result = CalcEngine.modulus(a, b)
        print(f"{a_str} % {b_str} = {result}")
