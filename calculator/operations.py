from decimal import Decimal, getcontext, InvalidOperation

# Set precision for decimal calculations
getcontext().prec = 28

class CalculationStrategy:
    """Base class for all calculation strategies."""
    def calculate(self, a: str, b: str) -> Decimal:
        raise NotImplementedError("Subclasses must implement the calculate method.")

class AdditionStrategy(CalculationStrategy):
    def calculate(self, a: str, b: str) -> Decimal:
        return Decimal(a) + Decimal(b)

class SubtractionStrategy(CalculationStrategy):
    def calculate(self, a: str, b: str) -> Decimal:
        return Decimal(a) - Decimal(b)

class MultiplicationStrategy(CalculationStrategy):
    def calculate(self, a: str, b: str) -> Decimal:
        return Decimal(a) * Decimal(b)

class DivisionStrategy(CalculationStrategy):
    def calculate(self, a: str, b: str) -> Decimal:
        try:
            return Decimal(a) / Decimal(b)
        except InvalidOperation:
            print("Error: Invalid input. Please enter numeric values.")
            return None
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
            return None

class Calculator:
    """Uses different calculation strategies dynamically."""
    def __init__(self, strategy: CalculationStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: CalculationStrategy):
        """Change the calculation strategy at runtime."""
        self.strategy = strategy

    def execute(self, a: str, b: str) -> Decimal:
        return self.strategy.calculate(a, b)
