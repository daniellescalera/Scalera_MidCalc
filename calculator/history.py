import pandas as pd

class CalculationHistory:
    """Manages calculation history using Pandas."""
    
    # ✅ Define history as a class attribute so all instances share it
    history = pd.DataFrame(columns=["Operation", "Operand1", "Operand2", "Result"])

    @classmethod
    def add_record(cls, operation: str, operand1: float, operand2: float, result: float):
        """Adds a new calculation record to the history."""
        new_record = pd.DataFrame([[operation, operand1, operand2, result]], 
                                  columns=cls.history.columns)
        cls.history = pd.concat([cls.history, new_record], ignore_index=True)

    @classmethod
    def save_history(cls, filename="history.csv"):
        """Saves history to a CSV file."""
        cls.history.to_csv(filename, index=False)

    @classmethod
    def load_history(cls, filename="history.csv"):
        """Loads history from a CSV file."""
        try:
            cls.history = pd.read_csv(filename)
        except FileNotFoundError:
            print("No previous history found.")

    @classmethod
    def clear_history(cls):
        """Clears the calculation history."""
        cls.history = pd.DataFrame(columns=["Operation", "Operand1", "Operand2", "Result"])

    @classmethod
    def get_last_calculation(cls):
        """Returns the last calculation from history, if available."""
        if not cls.history.empty:
            return cls.history.iloc[-1].to_dict()  # Returns last row as a dictionary
        else:
            return "📜 No calculations in history yet."
