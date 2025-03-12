import os
from dotenv import load_dotenv
from calculator.operations import Operations
from calculator.history import CalculationHistory

# Load environment variables from .env file
load_dotenv()

# Get environment variables
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")  # Default to INFO if not set
HISTORY_FILE = os.getenv("HISTORY_FILE", "history.csv")

class CalculatorREPL:
    """A simple command-line REPL for the calculator."""

    def __init__(self):
        self.history = CalculationHistory()
        print(f"Logging Level: {LOG_LEVEL}")
        print(f"History File: {HISTORY_FILE}")

    def start(self):
        """Start the REPL loop."""
        print("Welcome to the Calculator REPL! Type 'exit' to quit.")

        while True:
            command = input("Enter operation (add, subtract, multiply, divide, history, exit): ").strip().lower()

            if command == "exit":
                print("Goodbye!")
                break
            elif command == "history":
                print(self.history.history)
                continue

            try:
                num1 = input("Enter first number: ").strip()
                num2 = input("Enter second number: ").strip()

                if command == "add":
                    result = Operations.add(num1, num2)
                elif command == "subtract":
                    result = Operations.subtract(num1, num2)
                elif command == "multiply":
                    result = Operations.multiply(num1, num2)
                elif command == "divide":
                    result = Operations.divide(num1, num2)
                else:
                    print("Invalid command. Try again.")
                    continue

                self.history.add_record(command, num1, num2, result)
                print(f"Result: {result}")

            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    CalculatorREPL().start()