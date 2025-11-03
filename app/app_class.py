from decimal import Decimal
from app.plugins import square, power, modulus
from calculator.engine import CalcEngine
from app.plugins.root import Root
from app.plugins.int_divide import IntDivide
from app.plugins.percent import Percent
from app.plugins.abs_diff import AbsDiff


class App:
    """Main Calculator App."""

    def __init__(self):
        print("Calculator App Started\n")
        self.show_welcome()
        self.run_demo()
        self.command_loop()  # <-- Add this

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
        print(" - root")
        print(" - int_divide")
        print(" - percent")
        print(" - abs_diff")

        print("Type 'help' to show commands, 'exit' to quit.\n")

    def run_demo(self):
        print("Plugin Demo:")
        print("Square 5:", square.square_number(Decimal(5)))
        print("2 ^ 3:", power.power_numbers(Decimal(2), Decimal(3)))
        print("10 % 3:", modulus.mod_numbers(Decimal(10), Decimal(3)))
        print("Cube root of 27:", Root().calculate(Decimal(27), Decimal(3)))
        print("Integer Divide 10 // 3:", IntDivide().calculate(Decimal(10), Decimal(3)))
        print("Percentage 25 of 200:", Percent().calculate(Decimal(25), Decimal(200)))
        print("Absolute Difference 10 and 3:", AbsDiff().calculate(Decimal(10), Decimal(3)))


    def command_loop(self):
        """Interactive loop for user input."""
        while True:
            user_input = input("> ").strip()
            if not user_input:
                continue
            if user_input.lower() == "exit":
                print("Exiting Calculator. Bye!")
                break
            if user_input.lower() == "help":
                self.show_welcome()
                continue

            # Split command and arguments
            parts = user_input.split()
            command, *args = parts

            try:
                args = [Decimal(a) for a in args]
                if command == "square" and len(args) == 1:
                    print(square.square_number(args[0]))
                elif command == "power" and len(args) == 2:
                    print(power.power_numbers(args[0], args[1]))
                elif command == "modulus" and len(args) == 2:
                    print(modulus.mod_numbers(args[0], args[1]))
                elif command == "add" and len(args) == 2:
                    print(CalcEngine.sum_values(args[0], args[1]))
                elif command == "subtract" and len(args) == 2:
                    print(CalcEngine.difference(args[0], args[1]))
                elif command == "multiply" and len(args) == 2:
                    print(CalcEngine.product(args[0], args[1]))
                elif command == "divide" and len(args) == 2:
                    print(CalcEngine.quotient(args[0], args[1]))
                elif command == "root" and len(args) == 2:
                    print(Root().calculate(args[0], args[1]))
                elif command == "int_divide" and len(args) == 2:
                    print(IntDivide().calculate(args[0], args[1]))
                elif command == "percent" and len(args) == 2:
                    print(Percent().calculate(args[0], args[1]))
                elif command == "abs_diff" and len(args) == 2:
                    print(AbsDiff().calculate(args[0], args[1]))
                else:
                    print("Unknown command or wrong number of arguments.")
            except Exception as e:
                print("Error:", e)
    def run(self):
        while True:
            user_input = input("> ").strip()
            if user_input.lower() in ("exit", "quit"):
                break
            parts = user_input.split()
            if not parts:
                continue
            command = parts[0].lower()
            args = parts[1:]

            # Here is where you'll check commands and call CalcEngine methods

    