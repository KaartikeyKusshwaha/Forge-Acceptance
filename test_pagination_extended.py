import pytest
from pagination import validate_limit


def test_zero_rejected():
    """Regression: zero must be rejected."""
    with pytest.raises(ValueError):
        validate_limit(0)


def test_negative_rejected():
    """Negative values must be rejected."""
    with pytest.raises(ValueError):
        validate_limit(-1)
    with pytest.raises(ValueError):
        validate_limit(-100)


def test_above_max_rejected():
    """Values above 100 must be rejected."""
    with pytest.raises(ValueError):
        validate_limit(101)
    with pytest.raises(ValueError):
        validate_limit(1000)


def test_boundary_one_valid():
    """Boundary value 1 is valid."""
    assert validate_limit(1) == 1


def test_boundary_hundred_valid():
    """Boundary value 100 is valid."""
    assert validate_limit(100) == 100


def test_typical_valid():
    """Typical mid-range value is valid."""
    assert validate_limit(50) == 50
    assert validate_limit(20) == 20


def test_float_rejected():
    """Float values must be rejected even if numerically in range."""
    with pytest.raises(ValueError):
        validate_limit(20.5)
    with pytest.raises(ValueError):
        validate_limit(50.0)


def test_string_rejected():
    """String values must be rejected."""
    with pytest.raises(ValueError):
        validate_limit('20')
    with pytest.raises(ValueError):
        validate_limit('100')


def test_bool_rejected():
    """Bool values must be rejected (bool is a subclass of int)."""
    with pytest.raises(ValueError):
        validate_limit(True)
    with pytest.raises(ValueError):
        validate_limit(False)


def test_none_rejected():
    """None must be rejected."""
    with pytest.raises(ValueError):
        validate_limit(None)


def test_list_rejected():
    """List values must be rejected."""
    with pytest.raises(ValueError):
        validate_limit([20])
