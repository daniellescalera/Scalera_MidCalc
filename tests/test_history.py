import pytest
import pandas as pd
from unittest.mock import patch
from calculator.history import CalculationHistory
from calculator.facade import HistoryFacade  # Import facade for missing tests

@pytest.fixture
def history():
    """Fixture to provide a CalculationHistory instance."""
    return CalculationHistory()

def test_add_record(history):
    """Test adding a record to history."""
    history.add_record("add", 2, 3, 5)
    assert not history.history.empty
    assert len(history.history) == 1

def test_save_and_load_history(history, tmp_path):
    """Test saving and loading history from a file."""
    filename = tmp_path / "history.csv"

    # Clear history before running the test
    history.clear_history()

    history.add_record("multiply", 4, 3, 12)
    history.save_history(filename)

    # Create a new instance to test loading
    new_history = CalculationHistory()
    new_history.load_history(filename)

    # Check that only one record exists
    assert len(new_history.history) == 1
    assert new_history.history.iloc[0]["Result"] == 12

def test_clear_history(history):
    """Test clearing history."""
    history.add_record("subtract", 5, 2, 3)
    history.clear_history()
    assert history.history.empty

# Fix: Ensure `get_history()` is tested to cover Line 16 in facade.py
def test_facade_get_history():
    """Ensure HistoryFacade.get_history() retrieves the history DataFrame."""
    with patch("calculator.facade.HistoryFacade._history") as mock_history:
        mock_history.history = "Mocked History"  #  Fix: Directly set value
        result = HistoryFacade.get_history()
        assert result == "Mocked History"

# Fix: Cover `save_history()` in HistoryFacade
def test_facade_save_history():
    """Ensure HistoryFacade.save_history() calls CalculationHistory.save_history()."""
    with patch("calculator.history.CalculationHistory.save_history") as mock_save:
        HistoryFacade.save_history()
        mock_save.assert_called_once()

# Fix: Cover `load_history()` in HistoryFacade
def test_facade_load_history():
    """Ensure HistoryFacade.load_history() calls CalculationHistory.load_history()."""
    with patch("calculator.history.CalculationHistory.load_history") as mock_load:
        HistoryFacade.load_history()
        mock_load.assert_called_once()
