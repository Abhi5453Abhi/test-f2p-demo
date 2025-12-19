"""Tests for advanced calculator operations."""

import pytest
from calculator import (
    power, square_root, modulo, factorial, absolute, logarithm
)
from math_utils import (
    mean, median, mode, standard_deviation, gcd, lcm,
    is_prime, fibonacci, percentage, percentage_of
)
from calculator import Calculator


class TestAdvancedOperations:
    """Test advanced mathematical operations."""
    
    def test_power(self):
        """Test power operation."""
        assert power(2, 3) == 8
        assert power(5, 0) == 1
        assert power(2, -1) == 0.5
    
    def test_square_root(self):
        """Test square root operation."""
        assert square_root(4) == 2.0
        assert square_root(9) == 3.0
        assert square_root(0) == 0.0
    
    def test_square_root_negative(self):
        """Test square root with negative number raises error."""
        with pytest.raises(ValueError, match="Cannot calculate square root"):
            square_root(-1)
    
    def test_modulo(self):
        """Test modulo operation."""
        assert modulo(10, 3) == 1
        assert modulo(15, 5) == 0
        assert modulo(-10, 3) == 2
    
    def test_modulo_zero(self):
        """Test modulo with zero raises error."""
        with pytest.raises(ValueError, match="Cannot calculate modulo"):
            modulo(10, 0)
    
    def test_factorial(self):
        """Test factorial operation."""
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(5) == 120
    
    def test_factorial_negative(self):
        """Test factorial with negative number raises error."""
        with pytest.raises(ValueError, match="Factorial is not defined"):
            factorial(-1)
    
    def test_factorial_float(self):
        """Test factorial with float raises error."""
        with pytest.raises(TypeError, match="Factorial requires an integer"):
            factorial(5.5)
    
    def test_absolute(self):
        """Test absolute value."""
        assert absolute(-5) == 5
        assert absolute(5) == 5
        assert absolute(0) == 0
    
    def test_logarithm(self):
        """Test logarithm operation."""
        assert logarithm(1) == 0.0
        assert abs(logarithm(2.71828, 2.71828) - 1.0) < 0.01
    
    def test_logarithm_negative(self):
        """Test logarithm with negative number raises error."""
        with pytest.raises(ValueError, match="Logarithm is not defined"):
            logarithm(-1)
    
    def test_logarithm_zero(self):
        """Test logarithm with zero raises error."""
        with pytest.raises(ValueError, match="Logarithm is not defined"):
            logarithm(0)


class TestMathUtils:
    """Test mathematical utility functions."""
    
    def test_mean(self):
        """Test mean calculation."""
        assert mean([1, 2, 3, 4, 5]) == 3.0
        assert mean([10, 20, 30]) == 20.0
    
    def test_mean_empty(self):
        """Test mean with empty list raises error."""
        with pytest.raises(ValueError, match="Cannot calculate mean"):
            mean([])
    
    def test_median(self):
        """Test median calculation."""
        assert median([1, 3, 2]) == 2
        assert median([1, 2, 3, 4]) == 2.5
    
    def test_mode(self):
        """Test mode calculation."""
        assert mode([1, 2, 2, 3]) == 2
        result = mode([1, 1, 2, 2, 3])
        assert isinstance(result, list)
        assert set(result) == {1, 2}
    
    def test_standard_deviation(self):
        """Test standard deviation calculation."""
        assert abs(standard_deviation([1, 2, 3, 4, 5]) - 1.414) < 0.1
    
    def test_gcd(self):
        """Test greatest common divisor."""
        assert gcd(48, 18) == 6
        assert gcd(17, 13) == 1
    
    def test_lcm(self):
        """Test least common multiple."""
        assert lcm(12, 18) == 36
        assert lcm(5, 7) == 35
    
    def test_is_prime(self):
        """Test prime number detection."""
        assert is_prime(2) is True
        assert is_prime(17) is True
        assert is_prime(4) is False
        assert is_prime(1) is False
    
    def test_fibonacci(self):
        """Test Fibonacci sequence."""
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1
        assert fibonacci(5) == 5
        assert fibonacci(10) == 55
    
    def test_percentage(self):
        """Test percentage calculation."""
        assert percentage(25, 100) == 25.0
        assert percentage(50, 200) == 25.0
    
    def test_percentage_of(self):
        """Test percentage of calculation."""
        assert percentage_of(25, 100) == 25.0
        assert percentage_of(50, 200) == 100.0


class TestCalculatorClass:
    """Test Calculator class functionality."""
    
    def test_initialization(self):
        """Test calculator initialization."""
        calc = Calculator()
        assert calc.get_result() == 0
        calc2 = Calculator(10)
        assert calc2.get_result() == 10
    
    def test_add_operation(self):
        """Test add operation in calculator."""
        calc = Calculator()
        assert calc.add(5) == 5
        assert calc.add(3) == 8
    
    def test_subtract_operation(self):
        """Test subtract operation in calculator."""
        calc = Calculator(10)
        assert calc.subtract(3) == 7
        assert calc.subtract(2) == 5
    
    def test_multiply_operation(self):
        """Test multiply operation in calculator."""
        calc = Calculator(5)
        assert calc.multiply(3) == 15
        assert calc.multiply(2) == 30
    
    def test_divide_operation(self):
        """Test divide operation in calculator."""
        calc = Calculator(20)
        assert calc.divide(4) == 5.0
        assert calc.divide(2) == 2.5
    
    def test_power_operation(self):
        """Test power operation in calculator."""
        calc = Calculator(2)
        assert calc.power(3) == 8
        assert calc.power(2) == 64
    
    def test_reset(self):
        """Test calculator reset."""
        calc = Calculator(10)
        calc.add(5)
        assert calc.reset() == 0
        assert calc.reset(100) == 100
    
    def test_history(self):
        """Test operation history."""
        calc = Calculator()
        calc.add(5)
        calc.subtract(2)
        calc.multiply(3)
        history = calc.get_history()
        assert len(history) == 3
        assert history[0] == ('add', 5)
        assert history[1] == ('subtract', 2)
        assert history[2] == ('multiply', 3)
    
    def test_clear_history(self):
        """Test clearing history."""
        calc = Calculator()
        calc.add(5)
        calc.clear_history()
        assert len(calc.get_history()) == 0

