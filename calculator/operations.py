from decimal import Decimal, InvalidOperation

class Operations:
    """Performs basic arithmetic operations using Decimal for accuracy."""

    @staticmethod
    def add(a: str, b: str) -> Decimal:
        return Decimal(a) + Decimal(b)

    @staticmethod
    def subtract(a: str, b: str) -> Decimal:
        return Decimal(a) - Decimal(b)

    @staticmethod
    def multiply(a: str, b: str) -> Decimal:
        return Decimal(a) * Decimal(b)

    @staticmethod
    def divide(a: str, b: str) -> Decimal:
        """Returns the quotient of two numbers as Decimal, with exception handling."""
        try:
            return Decimal(a) / Decimal(b)
        except InvalidOperation:
            print("Error: Invalid input. Please enter numeric values.")
            return None
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
            return None
