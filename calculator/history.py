import pandas as pd

class CalculationHistory:
    """Manages calculation history using Pandas."""

    def __init__(self):
        self.history = pd.DataFrame(columns=["Operation", "Operand1", "Operand2", "Result"])

    def add_record(self, operation: str, operand1: float, operand2: float, result: float):
        """Adds a new calculation record to the history."""
        new_record = pd.DataFrame([[operation, operand1, operand2, result]], 
                                  columns=self.history.columns)
        self.history = pd.concat([self.history, new_record], ignore_index=True)

    def save_history(self, filename="history.csv"):
        """Saves history to a CSV file."""
        self.history.to_csv(filename, index=False)

    def load_history(self, filename="history.csv"):
        """Loads history from a CSV file."""
        try:
            self.history = pd.read_csv(filename)
        except FileNotFoundError:
            print("No previous history found.")

    def clear_history(self):
        """Clears the calculation history."""
        self.history = pd.DataFrame(columns=["Operation", "Operand1", "Operand2", "Result"])
