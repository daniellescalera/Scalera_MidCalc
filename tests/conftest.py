import pytest
from faker import Faker

@pytest.fixture(scope="session")
def fake():
    """Provides a Faker instance for generating test data."""
    return Faker()
