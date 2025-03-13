import os
from dotenv import load_dotenv
from calculator.operations import Operations
from calculator.history import CalculationHistory
from calculator.logger import logger  # Import the logger

# Load environment variables
load_dotenv()

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
HISTORY_FILE = os.getenv("HISTORY_FILE", "history.csv")

class CalculatorREPL:
    """A simple command-line REPL for the calculator."""

    def __init__(self):
        self.history = CalculationHistory()
        logger.info("Calculator REPL started")  # Log start of REPL
        print(f"Logging Level: {LOG_LEVEL}")
        print(f"History File: {HISTORY_FILE}")

    def start(self):
        """Start the REPL loop."""
        print("Welcome to the Calculator REPL! Type 'exit' to quit.")

        while True:
            command = input("Enter operation (add, subtract, multiply, divide, history, exit): ").strip().lower()
            logger.info(f"User entered command: {command}")

            if command == "exit":
                logger.info("User exited REPL")
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
                    logger.warning(f"Invalid command: {command}")
                    print("Invalid command. Try again.")
                    continue

                self.history.add_record(command, num1, num2, result)
                logger.info(f"Performed operation: {command} {num1} {num2} = {result}")
                print(f"Result: {result}")

            except Exception as e:
                logger.error(f"Error in REPL: {e}")
                print(f"Error: {e}")

if __name__ == "__main__":
    CalculatorREPL().start()
