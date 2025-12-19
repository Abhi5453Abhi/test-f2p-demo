"""Additional F2P tests specifically for modulo function bug fix.

These tests will FAIL on main branch (with bug) and PASS on fix branch.
"""

import pytest
from calculator import modulo


class TestModuloF2P:
    """F2P tests for modulo function negative number handling."""
    
    def test_modulo_negative_dividend_basic(self):
        """Test basic negative dividend - THIS IS F2P!"""
        # Main branch bug: returns -1, should return 2
        assert modulo(-10, 3) == 2
    
    def test_modulo_negative_dividend_various_cases(self):
        """Test various negative dividend cases - THIS IS F2P!"""
        test_cases = [
            (-10, 3, 2),
            (-25, 7, 3),
            (-1, 5, 4),
            (-100, 13, 4),
            (-7, 3, 2),
        ]
        for a, b, expected in test_cases:
            assert modulo(a, b) == expected, f"{a} % {b} should equal {expected}"
    
    def test_modulo_negative_dividend_edge_cases(self):
        """Test edge cases with negative dividends - THIS IS F2P!"""
        # Test with divisor = 1
        assert modulo(-5, 1) == 0
        # Test with divisor = 2
        assert modulo(-3, 2) == 1  # -3 % 2 = 1
        assert modulo(-4, 2) == 0  # -4 % 2 = 0
        # Test with large numbers
        assert modulo(-1000, 17) == 4  # -1000 % 17 = 4
    
    def test_modulo_negative_in_calculator_class(self):
        """Test modulo behavior in Calculator class - THIS IS F2P!"""
        from calculator import Calculator
        calc = Calculator(-10)
        # This should work correctly after fix
        result = calc.get_result()
        assert result == -10
        # Test that we can use modulo with negative result
        calc.add(5)  # Now -5
        # The modulo operation itself isn't in Calculator, but the bug affects
        # any code that uses modulo with negative numbers
        assert modulo(calc.get_result(), 3) == 1  # -5 % 3 = 1
    
    def test_modulo_consistency_with_positive(self):
        """Test that modulo is consistent - THIS IS F2P!"""
        # For positive numbers, both should work the same
        assert modulo(10, 3) == 1
        # For negative, should return positive remainder
        assert modulo(-10, 3) == 2
        # Relationship: (a % b) + ((-a) % b) should equal b when both are positive
        # Actually, let's test a different relationship
        assert modulo(-10, 3) == (3 - (10 % 3)) % 3 or modulo(-10, 3) == 2

