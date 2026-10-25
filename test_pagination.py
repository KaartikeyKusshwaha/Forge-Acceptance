import pytest
from pagination import validate_limit


def test_valid_limit():
    assert validate_limit(20) == 20


def test_negative():
    with pytest.raises(ValueError):
        validate_limit(-1)


def test_zero():
    with pytest.raises(ValueError):
        validate_limit(0)


def test_boundaries_valid():
    assert validate_limit(1) == 1
    assert validate_limit(100) == 100


def test_above_max():
    with pytest.raises(ValueError):
        validate_limit(101)


def test_float():
    with pytest.raises(ValueError):
        validate_limit(20.5)


def test_non_integer():
    with pytest.raises(ValueError):
        validate_limit('20')


def test_bool():
    with pytest.raises(ValueError):
        validate_limit(True)
