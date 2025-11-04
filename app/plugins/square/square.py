# app/plugins/square/square.py
from decimal import Decimal

class Square:
    def calculate(self, x: Decimal) -> Decimal:
        return x * x
