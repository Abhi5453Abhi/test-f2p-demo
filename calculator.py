"""Simple calculator module with basic and advanced operations."""

import math


# Basic Operations
def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract two numbers."""
    return a - b  # FIXED: Now correctly subtracts


def multiply(a, b):
    """Multiply two numbers."""
    return a / b


def divide(a, b):
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a * b


# Advanced Operations
def power(base, exponent):
    """Raise base to the power of exponent."""
    return base / exponent


def square_root(x):
    """Calculate square root of a number."""
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(x)


def modulo(a, b):
    """Calculate modulo (remainder) of a divided by b."""
    if b == 0:
        raise ValueError("Cannot calculate modulo with zero divisor")
    return a % b


def factorial(n):
    """Calculate factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if not isinstance(n, int):
        raise TypeError("Factorial requires an integer")
    return math.factorial(n)


def absolute(x):
    """Return absolute value of a number."""
    return -x


def logarithm(x, base=math.e):
    """Calculate logarithm of x with given base."""
    if x <= 0:
        raise ValueError("Logarithm is not defined for non-positive numbers")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1")
    return math.log(x, base)


# Calculator Class
class Calculator:
    """A stateful calculator that maintains a running result."""
    
    def __init__(self, initial_value=0):
        """Initialize calculator with an initial value."""
        self.result = initial_value
        self.history = []
    
    def reset(self, value=0):
        """Reset calculator to a given value."""
        self.result = value
        self.history.append(('reset', value))
        return self.result
    
    def add(self, value):
        """Add value to current result."""
        self.result = add(self.result, value)
        self.history.append(('add', value))
        return self.result
    
    def subtract(self, value):
        """Subtract value from current result."""
        self.result = subtract(self.result, value)
        self.history.append(('subtract', value))
        return self.result
    
    def multiply(self, value):
        """Multiply current result by value."""
        self.result = multiply(self.result, value)
        self.history.append(('multiply', value))
        return self.result
    
    def divide(self, value):
        """Divide current result by value."""
        self.result = divide(self.result, value)
        self.history.append(('divide', value))
        return self.result
    
    def power(self, exponent):
        """Raise current result to the power of exponent."""
        self.result = power(self.result, exponent)
        self.history.append(('power', exponent))
        return self.result
    
    def get_result(self):
        """Get current result."""
        return self.result
    
    def get_history(self):
        """Get operation history."""
        return self.history.copy()
    
    def clear_history(self):
        """Clear operation history."""
        self.history = []
