"""Tests for calculator module - specifically targeting the subtract bug fix."""
import pytest
from calculator import add, subtract, multiply, divide


def test_subtract_correct_result():
    """Test that subtract returns correct result - THIS IS F2P!"""
    # This test will FAIL on main branch (bug) and PASS on fix branch
    assert subtract(5, 3) == 2, "5 - 3 should equal 2"


def test_subtract_negative_result():
    """Test subtract with result being negative - THIS IS F2P!"""
    assert subtract(3, 5) == -2, "3 - 5 should equal -2"


def test_subtract_with_zero():
    """Test subtract with zero - THIS IS F2P!"""
    assert subtract(10, 0) == 10, "10 - 0 should equal 10"
    assert subtract(0, 10) == -10, "0 - 10 should equal -10"


def test_subtract_same_numbers():
    """Test subtract with same numbers - THIS IS F2P!"""
    assert subtract(5, 5) == 0, "5 - 5 should equal 0"


def test_subtract_negative_numbers():
    """Test subtract with negative numbers - THIS IS F2P!"""
    assert subtract(-5, -3) == -2, "-5 - -3 should equal -2"
    assert subtract(-5, 3) == -8, "-5 - 3 should equal -8"


# These tests will PASS on both branches (they test unchanged code)
def test_add_positive_numbers():
    """Test add with positive numbers - PASS-TO-PASS"""
    assert add(2, 3) == 5


def test_multiply_numbers():
    """Test multiply - PASS-TO-PASS"""
    assert multiply(3, 4) == 12


def test_divide_normal():
    """Test divide - PASS-TO-PASS"""
    assert divide(10, 2) == 5


def test_divide_by_zero_raises_error():
    """Test divide by zero raises error - PASS-TO-PASS"""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_add_negative_numbers():
    """Test add with negative numbers - PASS-TO-PASS"""
    assert add(-5, -3) == -8
    assert add(-5, 3) == -2


def test_multiply_with_zero():
    """Test multiply with zero - PASS-TO-PASS"""
    assert multiply(5, 0) == 0
    assert multiply(0, 10) == 0


def test_divide_decimal_result():
    """Test divide with decimal result - PASS-TO-PASS"""
    assert divide(7, 2) == 3.5
    assert divide(1, 3) == pytest.approx(0.333333, rel=1e-5)
