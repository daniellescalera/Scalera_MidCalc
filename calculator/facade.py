from calculator.history import CalculationHistory

class HistoryFacade:
    """Provides a simplified interface for managing calculation history."""

    _history = CalculationHistory()  # Use the Singleton instance

    @staticmethod
    def add_record(operation: str, operand1: float, operand2: float, result: float):
        """Adds a new record to history."""
        HistoryFacade._history.add_record(operation, operand1, operand2, result)

    @staticmethod
    def get_history():
        """Retrieves history as a DataFrame."""
        return HistoryFacade._history.history

    @staticmethod
    def save_history():
        """Saves history to a CSV file."""
        HistoryFacade._history.save_history()

    @staticmethod
    def load_history():
        """Loads history from a CSV file."""
        HistoryFacade._history.load_history()

    @staticmethod
    def clear_history():
        """Clears the calculation history."""
        HistoryFacade._history.clear_history()
