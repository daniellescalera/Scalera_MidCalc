"""
Main entry point for the calculator application.
Provides options to use the REPL or execute calculations directly.
"""

import argparse
from main.repl import CalculatorREPL
from main.use_calculator import main as use_calculator

def main():
    """Main function to choose between REPL mode and direct calculation mode."""
    parser = argparse.ArgumentParser(description="Calculator Application")
    parser.add_argument(
        "--mode",
        choices=["repl", "direct"],
        default="repl",
        help="Choose mode: 'repl' for interactive mode, 'direct' for direct calculation mode.",
    )
    args = parser.parse_args()

    if args.mode == "repl":
        print("Starting Calculator REPL...")
        CalculatorREPL().start()
    elif args.mode == "direct":
        print("Starting Direct Calculation Mode...")
        use_calculator()

if __name__ == "__main__":
    main()
