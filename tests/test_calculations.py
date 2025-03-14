import pytest
from calculator.calculations import Calculation

@pytest.mark.parametrize("operation, operand1, operand2, expected", [
    ("add", 5, 3, 8),          # 5 + 3 = 8
    ("subtract", 10, 4, 6),    # 10 - 4 = 6
    ("multiply", 2, 3, 6),     # 2 * 3 = 6
    ("divide", 8, 2, 4),       # 8 / 2 = 4
])
def test_calculation_operations(operation, operand1, operand2, expected):
    """Test Calculation class with different operations."""
    calc = Calculation(operation, operand1, operand2)
    assert calc.result == expected


def test_invalid_operation():
    """Test that invalid operations raise ValueError."""
    with pytest.raises(ValueError, match="Invalid operation: power"):
        Calculation("power", 2, 3)  # "power" is not a valid operation


def test_calculation_str():
    """Test string representation of Calculation object."""
    calc = Calculation("add", 4, 6)
    assert str(calc) == "4 add 6 = 10"
