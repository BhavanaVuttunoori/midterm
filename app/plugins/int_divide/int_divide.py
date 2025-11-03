# app/plugins/int_divide/int_divide.py

class IntDivide:
    name = "int_divide"  # command name

    def calculate(self, a, b):
        try:
            return a // b
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
        except Exception as e:
            return f"Error: {e}"
