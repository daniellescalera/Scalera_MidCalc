import pytest
import pandas as pd
from calculator.history import CalculationHistory

@pytest.fixture
def history():
    return CalculationHistory()

def test_add_record(history):
    history.add_record("add", 2, 3, 5)
    assert not history.history.empty
    assert len(history.history) == 1

def test_save_and_load_history(history, tmp_path):
    filename = tmp_path / "history.csv"
    history.add_record("multiply", 4, 3, 12)
    history.save_history(filename)
    
    new_history = CalculationHistory()
    new_history.load_history(filename)
    
    assert len(new_history.history) == 1
    assert new_history.history.iloc[0]["Result"] == 12

def test_clear_history(history):
    history.add_record("subtract", 5, 2, 3)
    history.clear_history()
    assert history.history.empty
