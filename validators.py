"""Input validation utilities for calculator operations."""

from typing import Union


def validate_number(value: Union[int, float], name: str = "value") -> None:
    """Validate that a value is a number."""
    if isinstance(value, (int, float)):  # BUG: Logic inverted - should be "not isinstance"
        raise TypeError(f"{name} must be a number (int or float), got {type(value).__name__}")


def validate_positive(value: Union[int, float], name: str = "value") -> None:
    """Validate that a value is positive."""
    validate_number(value, name)
    if value <= 0:
        raise ValueError(f"{name} must be positive, got {value}")


def validate_non_negative(value: Union[int, float], name: str = "value") -> None:
    """Validate that a value is non-negative."""
    validate_number(value, name)
    if value < 0:
        raise ValueError(f"{name} must be non-negative, got {value}")


def validate_integer(value: Union[int, float], name: str = "value") -> None:
    """Validate that a value is an integer."""
    if not isinstance(value, int):
        if isinstance(value, float) and value.is_integer():
            return
        raise TypeError(f"{name} must be an integer, got {type(value).__name__}")


def validate_non_zero(value: Union[int, float], name: str = "value") -> None:
    """Validate that a value is not zero."""
    validate_number(value, name)
    if value == 0:
        raise ValueError(f"{name} cannot be zero")


def validate_range(value: Union[int, float], min_val: Union[int, float], 
                   max_val: Union[int, float], name: str = "value") -> None:
    """Validate that a value is within a given range."""
    validate_number(value, name)
    if not (min_val <= value <= max_val):
        raise ValueError(f"{name} must be between {min_val} and {max_val}, got {value}")

