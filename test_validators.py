"""Tests for validation utilities."""

import pytest
from validators import (
    validate_number, validate_positive, validate_non_negative,
    validate_integer, validate_non_zero, validate_range
)


class TestValidators:
    """Test input validation functions."""
    
    def test_validate_number_int(self):
        """Test validate_number with integer."""
        validate_number(5)
        validate_number(-10)
    
    def test_validate_number_float(self):
        """Test validate_number with float."""
        validate_number(5.5)
        validate_number(-10.2)
    
    def test_validate_number_invalid(self):
        """Test validate_number with invalid type."""
        with pytest.raises(TypeError):
            validate_number("5")
        with pytest.raises(TypeError):
            validate_number([1, 2, 3])
    
    def test_validate_positive(self):
        """Test validate_positive."""
        validate_positive(5)
        validate_positive(0.1)
    
    def test_validate_positive_invalid(self):
        """Test validate_positive with invalid values."""
        with pytest.raises(ValueError):
            validate_positive(0)
        with pytest.raises(ValueError):
            validate_positive(-5)
    
    def test_validate_non_negative(self):
        """Test validate_non_negative."""
        validate_non_negative(0)
        validate_non_negative(5)
    
    def test_validate_non_negative_invalid(self):
        """Test validate_non_negative with negative."""
        with pytest.raises(ValueError):
            validate_non_negative(-1)
    
    def test_validate_integer(self):
        """Test validate_integer."""
        validate_integer(5)
        validate_integer(0)
    
    def test_validate_integer_float(self):
        """Test validate_integer with float raises error."""
        with pytest.raises(TypeError):
            validate_integer(5.5)
    
    def test_validate_non_zero(self):
        """Test validate_non_zero."""
        validate_non_zero(5)
        validate_non_zero(-5)
    
    def test_validate_non_zero_invalid(self):
        """Test validate_non_zero with zero."""
        with pytest.raises(ValueError):
            validate_non_zero(0)
    
    def test_validate_range(self):
        """Test validate_range."""
        validate_range(5, 0, 10)
        validate_range(0, 0, 10)
        validate_range(10, 0, 10)
    
    def test_validate_range_invalid(self):
        """Test validate_range with out of range values."""
        with pytest.raises(ValueError):
            validate_range(-1, 0, 10)
        with pytest.raises(ValueError):
            validate_range(11, 0, 10)

