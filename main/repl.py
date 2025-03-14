import os
from dotenv import load_dotenv
from calculator.facade import HistoryFacade
from calculator.logger import logger
from calculator.plugin_factory import PluginFactory
from calculator.operations import Calculator, AdditionStrategy, SubtractionStrategy, MultiplicationStrategy, DivisionStrategy

# Load environment variables
load_dotenv()

environment = os.getenv("ENVIRONMENT", "Production")  # Default to "Production" if missing
print(f"\nRunning in {environment} mode")  # Display environment mode

class CalculatorREPL:
    """A command-line REPL for the calculator with commands and arithmetic operations."""

    def __init__(self):
        self.plugins = self.load_plugins()
        logger.info("Calculator REPL started")
        HistoryFacade.load_history()  # Automatically load history on startup

    def load_plugins(self):
        """Uses the Factory Pattern to load plugins dynamically."""
        return PluginFactory.load_plugins()

    def show_menu(self):
        """Displays available commands including plugins."""
        print("\nAvailable Commands:")
        print("  add, subtract, multiply, divide - Perform calculations")
        print("  history - View past calculations")
        print("  save - Save history to file")
        print("  load - Load history from file")
        print("  menu - Show this menu")
        print("  exit - Quit the calculator")

        # List plugin commands
        if self.plugins:
            print("\nPlugin Commands:")
            for command, plugin in self.plugins.items():
                print(f"  {command} - {plugin['description']}")

    def start(self):
        """Start the REPL loop."""
        print("\nWelcome to the Advanced Calculator! Type 'menu' for options.")

        strategy_map = {
            "add": AdditionStrategy(),
            "subtract": SubtractionStrategy(),
            "multiply": MultiplicationStrategy(),
            "divide": DivisionStrategy()
        }

        while True:
            user_input = input("\nEnter operation: ").strip().lower()

            if user_input in ["exit", "quit"]:
                print("Goodbye!")
                logger.info("Calculator REPL exited.")
                break
            elif user_input == "menu":
                self.show_menu()
            elif user_input == "history":
                if not HistoryFacade.get_history().empty:
                    print("\nCalculation History:")
                    print(HistoryFacade.get_history().to_string(index=False))
                else:
                    print("\nNo calculations in history yet.")
            elif user_input == "save":
                HistoryFacade.save_history()
            elif user_input == "load":
                HistoryFacade.load_history()
            elif user_input in strategy_map:  # Use Strategy Pattern for calculations
                try:
                    num1 = input("Enter the first number: ").strip()
                    num2 = input("Enter the second number: ").strip()

                    calculator = Calculator(strategy_map[user_input])  # Use the selected strategy
                    result = calculator.execute(num1, num2)

                    if result is not None:  # Ensure we don't store failed operations
                        print(f"Result: {result}")
                        HistoryFacade.add_record(user_input, num1, num2, result)
                except Exception as e:
                    print(f"Error: {e}")
                    logger.error(f"Operation {user_input} failed: {e}")
            elif user_input in self.plugins:
                plugin = self.plugins[user_input]
                try:
                    num_args = int(input(f"How many numbers does {user_input} need? ").strip())
                    args = [float(input(f"Enter number {i + 1}: ").strip()) for i in range(num_args)]

                    result = plugin["function"](*args)
                    print(f"Result: {result}")
                    HistoryFacade.add_record(user_input, *args, result)
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
                    logger.error(f"Invalid input for plugin {user_input}.")
                except Exception as e:
                    print(f"Error: {e}")
                    logger.error(f"Plugin {user_input} failed: {e}")
            else:
                print("Unknown command. Type 'menu' to see available commands.")

if __name__ == "__main__":
    repl = CalculatorREPL()
    repl.start()
