import pytest
from unittest.mock import patch
import main.repl

@pytest.fixture
def repl():
    """Fixture to create a REPL instance."""
    return main.repl.CalculatorREPL()

def test_plugin_loading(repl):
    """Test if plugins are loaded into REPL."""
    assert "power" in repl.plugins  # Ensure 'power' plugin is detected

@patch("builtins.input", side_effect=["power", "2", "2", "3", "exit"])
def test_power_plugin_execution(mock_input, repl, capsys):
    """Test the 'power' plugin execution."""
    repl.start()  # Start REPL with simulated input

    captured = capsys.readouterr()  # Capture REPL output once
    assert "Result: 8.0" in captured.out  # Ensure power calculation works correctly
