import pytest
from decimal import Decimal
from calculator.operations import (
    CalculationStrategy,
    AdditionStrategy,
    SubtractionStrategy,
    MultiplicationStrategy,
    DivisionStrategy,
    Calculator,
)

def test_calculation_strategy_not_implemented():
    """Ensure CalculationStrategy raises NotImplementedError."""
    strategy = CalculationStrategy()
    with pytest.raises(NotImplementedError, match="Subclasses must implement the calculate method."):
        strategy.calculate("1", "2")

@pytest.mark.parametrize("strategy_class, a, b, expected", [
    (AdditionStrategy, "5", "3", Decimal("8")),     # 5 + 3 = 8
    (SubtractionStrategy, "10", "4", Decimal("6")), # 10 - 4 = 6
    (MultiplicationStrategy, "2", "3", Decimal("6")), # 2 * 3 = 6
    (DivisionStrategy, "8", "2", Decimal("4")),     # 8 / 2 = 4
])
def test_calculator_operations(strategy_class, a, b, expected):
    """Test different calculation strategies with Calculator."""
    strategy = strategy_class()
    calculator = Calculator(strategy)
    assert calculator.execute(a, b) == expected

# ✅ Fix: Expect ValueError instead of None
def test_divide_by_zero():
    """Ensure division by zero raises ValueError."""
    calculator = Calculator(DivisionStrategy())
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calculator.execute("10", "0")

# ✅ Fix: Expect ValueError for invalid input
@pytest.mark.parametrize("a, b", [
    ("abc", "5"),  # Non-numeric input
    ("5", "xyz"),
    ("abc", "xyz"),
])
def test_division_invalid_input(a, b):
    """Ensure DivisionStrategy raises ValueError for invalid input."""
    calculator = Calculator(DivisionStrategy())
    with pytest.raises(ValueError, match="Invalid input. Please enter numeric values."):
        calculator.execute(a, b)
