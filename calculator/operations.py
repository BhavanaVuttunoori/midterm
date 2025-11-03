"""
Operations Module with CalcEngine Wrapper.

Provides basic arithmetic functions including addition, subtraction,
multiplication, division, squaring, power, and modulus, using Decimal precision.
"""

from decimal import Decimal


# Standalone functions for operations
def add_numbers(x: Decimal, y: Decimal) -> Decimal:
    return x + y

def sub_numbers(x: Decimal, y: Decimal) -> Decimal:
    return x - y

def mul_numbers(x: Decimal, y: Decimal) -> Decimal:
    return x * y

def div_numbers(x: Decimal, y: Decimal) -> Decimal:
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def square_number(x: Decimal) -> Decimal:
    return x * x

def power_numbers(x: Decimal, y: Decimal) -> Decimal:
    return x ** y

def mod_numbers(x: Decimal, y: Decimal) -> Decimal:
    if y == 0:
        raise ValueError("Cannot perform modulus with zero divisor")
    return x % y


# CalcEngine class wrapper for plugins
class CalcEngine:
    @staticmethod
    def add(x: Decimal, y: Decimal) -> Decimal:
        return add_numbers(x, y)

    @staticmethod
    def subtract(x: Decimal, y: Decimal) -> Decimal:
        return sub_numbers(x, y)

    @staticmethod
    def multiply(x: Decimal, y: Decimal) -> Decimal:
        return mul_numbers(x, y)

    @staticmethod
    def divide(x: Decimal, y: Decimal) -> Decimal:
        return div_numbers(x, y)

    @staticmethod
    def square(x: Decimal) -> Decimal:
        return square_number(x)

    @staticmethod
    def power(x: Decimal, y: Decimal) -> Decimal:
        return power_numbers(x, y)

    @staticmethod
    def modulus(x: Decimal, y: Decimal) -> Decimal:
        return mod_numbers(x, y)
