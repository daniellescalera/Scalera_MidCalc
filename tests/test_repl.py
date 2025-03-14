import pytest
from io import StringIO
from calculator.facade import HistoryFacade
import main.repl
from unittest.mock import patch

@pytest.fixture
def repl():
    return main.repl.CalculatorREPL()

def test_menu_command(repl, capsys):
    """Test if REPL correctly displays the menu."""
    repl.show_menu()
    captured = capsys.readouterr()
    assert "Available Commands:" in captured.out

def test_history_command(repl, capsys):
    """Test if REPL correctly displays history."""
    HistoryFacade.clear_history()  # Ensure history is empty
    repl.show_menu()
    
    captured = capsys.readouterr()
    assert "history - View past calculations" in captured.out

@patch("builtins.input", side_effect=["exit"])
def test_exit_command(mock_input, repl, capsys):
    """Test if REPL prints 'Goodbye!' when exiting."""
    repl.start()  # Start REPL with "exit" as input
    captured = capsys.readouterr()
    assert "Goodbye!" in captured.out  # Check if "Goodbye!" was printed

@patch("builtins.input", side_effect=["invalid_command", "exit"])
def test_invalid_command(mock_input, repl, capsys):
    """Test how REPL handles an invalid command."""
    repl.start()  # Start REPL with "invalid_command" followed by "exit"
    captured = capsys.readouterr()
    assert "Unknown command. Type 'menu' to see available commands." in captured.out
