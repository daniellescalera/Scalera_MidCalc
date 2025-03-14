from decimal import Decimal, getcontext, InvalidOperation

# Set precision for decimal calculations
getcontext().prec = 28

class CalculationStrategy:
    """Base class for all calculation strategies."""
    def calculate(self, a: str, b: str) -> Decimal:
        """Abstract method that must be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement the calculate method.")

class AdditionStrategy(CalculationStrategy):
    """Performs addition operation."""
    def calculate(self, a: str, b: str) -> Decimal:
        return Decimal(a) + Decimal(b)

class SubtractionStrategy(CalculationStrategy):
    """Performs subtraction operation."""
    def calculate(self, a: str, b: str) -> Decimal:
        return Decimal(a) - Decimal(b)

class MultiplicationStrategy(CalculationStrategy):
    """Performs multiplication operation."""
    def calculate(self, a: str, b: str) -> Decimal:
        return Decimal(a) * Decimal(b)

class DivisionStrategy(CalculationStrategy):
    """Performs division operation with error handling."""
    def calculate(self, a: str, b: str) -> Decimal:
        try:
            return Decimal(a) / Decimal(b)
        except InvalidOperation:
            raise ValueError("Invalid input. Please enter numeric values.")  # ✅ Updated: Raise ValueError instead of print
        except ZeroDivisionError:
            raise ValueError("Cannot divide by zero.")  # ✅ Updated: Raise ValueError instead of print

class Calculator:
    """Uses different calculation strategies dynamically."""
    def __init__(self, strategy: CalculationStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: CalculationStrategy):
        """Change the calculation strategy at runtime."""
        self.strategy = strategy

    def execute(self, a: str, b: str) -> Decimal:
        """Executes the strategy's calculation method."""
        return self.strategy.calculate(a, b)
