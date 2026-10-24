import pytest
from pagination import validate_limit

def test_valid_limit():
    assert validate_limit(20) == 20

def test_negative():
    with pytest.raises(ValueError):
        validate_limit(-1)
