import pytest
from Hexorcist import to_decimal, from_decimal

def test_to_decimal_basic():
    assert to_decimal("10", 2) == 2
    assert to_decimal("FF", 16) == 255
    assert to_decimal("Z", 36) == 35
    assert to_decimal("0", 10) == 0

def test_from_decimal_basic():
    assert from_decimal(2, 2) == "10"
    assert from_decimal(255, 16) == "FF"
    assert from_decimal(35, 36) == "Z"
    assert from_decimal(0, 2) == "0"

def test_round_trip():
    cases = [("101", 2, 16), ("FF", 16, 2), ("123", 10, 16), ("Z", 36, 10)]
    for num, orig_base, target_base in cases:
        decimal = to_decimal(num, orig_base)
        converted = from_decimal(decimal, target_base)
        assert to_decimal(converted, target_base) == decimal
