# app/plugins/root/root.py


class Root:
    name = "root"  # command name

    def calculate(self, a, n):
        try:
            return a ** (1 / n)
        except ZeroDivisionError:
            return "Error: Root degree cannot be zero."
        except Exception as e:
            return f"Error: {e}"
