import pytest
from decimal import Decimal
from calculator.operations import Operations

def test_add(fake):
    a, b = fake.pyfloat(min_value=1, max_value=100), fake.pyfloat(min_value=1, max_value=100)
    assert Operations.add(str(a), str(b)) == Decimal(str(a)) + Decimal(str(b))

def test_subtract(fake):
    a, b = fake.pyfloat(min_value=1, max_value=100), fake.pyfloat(min_value=1, max_value=100)
    assert Operations.subtract(str(a), str(b)) == Decimal(str(a)) - Decimal(str(b))

def test_multiply(fake):
    a, b = fake.pyfloat(min_value=1, max_value=100), fake.pyfloat(min_value=1, max_value=100)
    assert Operations.multiply(str(a), str(b)) == Decimal(str(a)) * Decimal(str(b))

def test_divide(fake):
    a, b = fake.pyfloat(min_value=1, max_value=100), fake.pyfloat(min_value=1, max_value=100, exclude=[0])
    assert Operations.divide(str(a), str(b)) == Decimal(str(a)) / Decimal(str(b))

def test_divide_by_zero():
    assert Operations.divide("10", "0") is None  # Should return None instead of crashing

def test_invalid_input():
    assert Operations.divide("abc", "2") is None  # Should handle non-numeric input
