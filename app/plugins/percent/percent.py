# app/plugins/percent/percent.py

class Percent:
    name = "percent"  # command name

    def calculate(self, a, b):
        try:
            return (a / b) * 100
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
        except Exception as e:
            return f"Error: {e}"
