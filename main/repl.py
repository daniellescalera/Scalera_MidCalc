import os
import importlib
from dotenv import load_dotenv
from calculator.operations import Operations
from calculator.calculations import Calculation
from calculator.history import CalculationHistory
from calculator.logger import logger

# Load environment variables
load_dotenv()

environment = os.getenv("ENVIRONMENT", "Production")  # Default to "Production" if missing
print(f"\nRunning in {environment} mode")  # Display environment mode

class CalculatorREPL:
    """A command-line REPL for the calculator with commands and arithmetic operations."""

    def __init__(self):
        self.plugins = self.load_plugins()
        logger.info("Calculator REPL started")  # Log REPL startup

    def load_plugins(self):
        """Dynamically loads all plugins from the plugins/ folder."""
        plugins = {}
        plugin_dir = "plugins"
        if os.path.exists(plugin_dir):
            for filename in os.listdir(plugin_dir):
                if filename.endswith(".py") and filename != "__init__.py":
                    module_name = f"plugins.{filename[:-3]}"  # Remove .py extension
                    module = importlib.import_module(module_name)
                    if hasattr(module, "plugin_info"):
                        info = module.plugin_info()
                        plugins[info["command"]] = info
        return plugins

    def show_menu(self):
        """Displays available commands including plugins."""
        print("\nAvailable Commands:")
        print("  add, subtract, multiply, divide - Perform calculations")
        print("  history - View past calculations")
        print("  clear - Clear history")
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

        while True:
            user_input = input("\nEnter operation: ").strip().lower()

            if user_input in ["exit", "quit"]:
                print("Goodbye!")
                logger.info("Calculator REPL exited.")
                break
            elif user_input == "menu":
                self.show_menu()
            elif user_input == "history":
                if not CalculationHistory.history.empty:
                    print("\nCalculation History:")
                    print(CalculationHistory.history.to_string(index=False))
                else:
                    print("\nNo calculations in history yet.")
            elif user_input == "save":
                CalculationHistory.save_history()
            elif user_input == "load":
                CalculationHistory.load_history()
            elif user_input in ["add", "subtract", "multiply", "divide"]:
                try:
                    num1 = float(input("Enter the first number: ").strip())
                    num2 = float(input("Enter the second number: ").strip())

                    if user_input == "divide" and num2 == 0:
                        raise ZeroDivisionError("Cannot divide by zero.")

                    result = getattr(Operations, user_input)(num1, num2)
                    print(f"Result: {result}")

                    CalculationHistory.add_record(user_input, num1, num2, result)
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
                    logger.error(f"Invalid input for {user_input} operation.")
                except ZeroDivisionError as e:
                    print(f"Error: {e}")
                    logger.error("Attempted division by zero.")
                except Exception as e:
                    print(f"Error: {e}")
                    logger.error(f"Operation {user_input} failed: {e}")
            elif user_input in self.plugins:
                plugin = self.plugins[user_input]
                try:
                    if user_input == "power":
                        #ensure power always takes exactly 2 arguments
                        num1 = float(input("Enter the base: ").strip())
                        num2 = float(input("Enter the exponent: ").strip())
                        result = plugin["function"](num1, num2)
                    else:
                        num_args = int(input(f"How many numbers does {user_input} need? ").strip())
                        args = [float(input(f"Enter number {i + 1}: ").strip()) for i in range(num_args)]
                        result = plugin["function"](*args)
                    print(f"Result: {result}")
                    CalculationHistory.add_record(user_input, num1, num2, result)       
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
                    logger.error(f"Invalid input for plugin {user_input}.")
                except TypeError as e:
                    print(f"Error: {e}")
                    logger.error(f"Plugin {user_input} failed: {e}")
                except Exception as e:
                    print(f"Error: {e}")
                    logger.error(f"Plugin {user_input} failed: {e}")
            else:
                print("Unknown command. Type 'menu' to see available commands.")

if __name__ == "__main__":
    repl = CalculatorREPL()
    repl.start()