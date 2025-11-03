# app/plugins/abs_diff/abs_diff.py

class AbsDiff:
    name = "abs_diff"  # command name

    def calculate(self, a, b):
        try:
            return abs(a - b)
        except Exception as e:
            return f"Error: {e}"
