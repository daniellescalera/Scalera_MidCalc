import pandas as pd

class CalculationHistory:
    """Manages calculation history using Pandas, implemented as a Singleton."""

    _instance = None  # Store the single instance

    def __new__(cls):
        """Ensures only one instance of CalculationHistory exists."""
        if cls._instance is None:
            cls._instance = super(CalculationHistory, cls).__new__(cls)
            cls._instance.history = pd.DataFrame(columns=["Operation", "Operand1", "Operand2", "Result"])
        return cls._instance

    def add_record(self, operation: str, operand1: float, operand2: float, result: float):
        """Adds a new calculation record to the history while handling empty DataFrames properly."""
        new_record = pd.DataFrame([[operation, operand1, operand2, result]], columns=self.history.columns)

        if self.history.empty:
            self.history = new_record
        else:
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

    def get_last_calculation(self):
        """Returns the last calculation from history, if available."""
        if not self.history.empty:
            return self.history.iloc[-1].to_dict()  # Returns last row as a dictionary
        else:
            return "No calculations in history yet."
