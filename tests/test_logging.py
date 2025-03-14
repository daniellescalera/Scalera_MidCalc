import logging
import pytest
from unittest.mock import patch
from main.repl import CalculatorREPL

@pytest.fixture
def repl(caplog):
    """Fixture to create a new instance of the REPL for testing."""
    with caplog.at_level(logging.INFO, logger="calculator.logger"):
        caplog.clear()
        return CalculatorREPL()

def test_logging_startup(caplog):
    """Test if REPL logs when it starts."""

    with caplog.at_level(logging.INFO, logger="calculator.logger"):
        caplog.clear()  # Clear previous logs before capturing
        repl = CalculatorREPL()  # Capture logs when REPL starts

        with patch("builtins.input", side_effect=["menu", "exit"]):
            repl.start()

    logs = caplog.text
    print("\nCaptured Logs:\n", logs)

    assert "Calculator REPL started" in logs


def test_logging_invalid_command(repl, caplog):
    """Test if invalid commands are logged."""
    with patch("builtins.input", side_effect=["invalid_command", "exit"]):
        with caplog.at_level(logging.WARNING, logger="main.repl"):
            repl.start()

    logs = caplog.text
    assert "Invalid command" in logs

def test_logging_invalid_input(repl, caplog):
    """Test if invalid input for an operation is logged."""
    with patch("builtins.input", side_effect=["add", "a", "b", "exit"]):
        with caplog.at_level(logging.ERROR, logger="main.repl"):
            repl.start()

    logs = caplog.text
    assert "Invalid input. Please enter numeric values." in logs or "Operation add failed" in logs
