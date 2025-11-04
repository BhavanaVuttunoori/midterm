from decimal import Decimal
from app.plugins.square.square import Square

def test_square():
    s = Square()
    assert s.calculate(Decimal(3)) == 9
