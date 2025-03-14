from calculator.operations import Calculator, AdditionStrategy, SubtractionStrategy, MultiplicationStrategy, DivisionStrategy

class Calculation:
    """Handles storing and executing calculations using the Strategy Pattern."""

    def __init__(self, operation, operand1, operand2):
        self.operation = operation
        self.operand1 = operand1
        self.operand2 = operand2
        self.result = self.execute()

    def execute(self):
        """Executes the stored operation using the Strategy Pattern and returns the result."""
        strategy_map = {
            "add": AdditionStrategy(),
            "subtract": SubtractionStrategy(),
            "multiply": MultiplicationStrategy(),
            "divide": DivisionStrategy()
        }

        if self.operation not in strategy_map:
            raise ValueError(f"Invalid operation: {self.operation}")

        calculator = Calculator(strategy_map[self.operation])
        return calculator.execute(self.operand1, self.operand2)

    def __str__(self):
        return f"{self.operand1} {self.operation} {self.operand2} = {self.result}"
