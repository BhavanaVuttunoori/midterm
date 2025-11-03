# app/app_class.py

from decimal import Decimal
from app.plugins import square, power, modulus
from calculator.engine import CalcEngine

class App:
    """Main Calculator App."""

    def __init__(self):
        print("Calculator App Started\n")
        self.show_welcome()
        self.run_demo()

    def show_welcome(self):
        print("Welcome to Calculator!\n")
        print("Available commands:")
        print(" - add")
        print(" - subtract")
        print(" - multiply")
        print(" - divide")
        print(" - square")
        print(" - power")
        print(" - modulus")
        print("Type 'help' to show commands, 'exit' to quit.\n")

    def run_demo(self):
        # Just a demo of plugin operations
        print("Plugin Demo:")
        print("Square 5:", square.square_number(Decimal(5)))
        print("2 ^ 3:", power.power_numbers(Decimal(2), Decimal(3)))
        print("10 % 3:", modulus.mod_numbers(Decimal(10), Decimal(3)))
