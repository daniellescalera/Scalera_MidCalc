from decimal import Decimal, getcontext

# Set precision for decimal calculations
getcontext().prec = 28

class Operations:
    #Performs basic arithmetic operations using Decimal for accuracy.

    @staticmethod
    def add(a: str, b: str) -> Decimal:
        #Returns the sum of two numbers as Decimal.
        return Decimal(a) + Decimal(b)

    @staticmethod
    def subtract(a: str, b: str) -> Decimal:
        #Returns the difference between two numbers as Decimal.
        return Decimal(a) - Decimal(b)

    @staticmethod
    def multiply(a: str, b: str) -> Decimal:
        #Returns the product of two numbers as Decimal.
        return Decimal(a) * Decimal(b)

    @staticmethod
    def divide(a: str, b: str) -> Decimal:
        #Returns the quotient of two numbers as Decimal. Raises error on divide by zero.
        if Decimal(b) == Decimal("0"):
            raise ZeroDivisionError("Cannot divide by zero")
        return Decimal(a) / Decimal(b)