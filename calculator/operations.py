from decimal import Decimal, getcontext, InvalidOperation  # Add InvalidOperation

# Set precision for decimal calculations
getcontext().prec = 28

class Operations:
    """Performs basic arithmetic operations using Decimal for accuracy."""

    @staticmethod
    def add(a: str, b: str) -> Decimal:
        """Returns the sum of two numbers as Decimal."""
        return Decimal(a) + Decimal(b)

    @staticmethod
    def subtract(a: str, b: str) -> Decimal:
        """Returns the difference between two numbers as Decimal."""
        return Decimal(a) - Decimal(b)

    @staticmethod
    def multiply(a: str, b: str) -> Decimal:
        """Returns the product of two numbers as Decimal."""
        return Decimal(a) * Decimal(b)

    @staticmethod
    def divide(a: str, b: str) -> Decimal:
        """Handles division with exception handling."""
        try:
            return Decimal(a) / Decimal(b)
        except InvalidOperation:  # ✅ Exception handling for invalid inputs
            print("Error: Invalid input. Please enter numeric values.")
            return None
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
            return None
