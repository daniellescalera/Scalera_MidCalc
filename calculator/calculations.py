from calculator.operations import Operations

class Calculation:
    """Handles storing and executing calculations."""

    def __init__(self, operation, operand1, operand2):
        self.operation = operation
        self.operand1 = operand1
        self.operand2 = operand2
        self.result = self.execute()

    def execute(self):
        """Executes the stored operation and returns the result."""
        if self.operation == "add":
            return Operations.add(self.operand1, self.operand2)
        elif self.operation == "subtract":
            return Operations.subtract(self.operand1, self.operand2)
        elif self.operation == "multiply":
            return Operations.multiply(self.operand1, self.operand2)
        elif self.operation == "divide":
            return Operations.divide(self.operand1, self.operand2)
        else:
            raise ValueError(f"Invalid operation: {self.operation}")

    def __str__(self):
        return f"{self.operand1} {self.operation} {self.operand2} = {self.result}"
