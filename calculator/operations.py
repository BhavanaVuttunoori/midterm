"""
Operations Module.

Provides basic arithmetic functions including addition, subtraction,
multiplication, division, squaring, power, and modulus, using Decimal precision.
"""

from decimal import Decimal


def add_numbers(x: Decimal, y: Decimal) -> Decimal:
    """Return the sum of two decimal numbers."""
    return x + y


def sub_numbers(x: Decimal, y: Decimal) -> Decimal:
    """Return the difference between two decimal numbers."""
    return x - y


def mul_numbers(x: Decimal, y: Decimal) -> Decimal:
    """Return the product of two decimal numbers."""
    return x * y


def div_numbers(x: Decimal, y: Decimal) -> Decimal:
    """
    Return the quotient of two decimal numbers.

    Raises:
        ValueError: If divisor is zero.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y


def square_number(x: Decimal) -> Decimal:
    """Return the square of a decimal number."""
    return x * x


def power_numbers(x: Decimal, y: Decimal) -> Decimal:
    """Return x raised to the power of y."""
    return x ** y


def mod_numbers(x: Decimal, y: Decimal) -> Decimal:
    """
    Return the modulus (remainder) of x divided by y.

    Raises:
        ValueError: If divisor is zero.
    """
    if y == 0:
        raise ValueError("Cannot perform modulus with zero divisor")
    return x % y
