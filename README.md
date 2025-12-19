# Calculator Demo

A comprehensive calculator package for F2P (Fail-to-Pass) testing demo.

## Features

### Basic Operations
- `add(a, b)` - Add two numbers
- `subtract(a, b)` - Subtract two numbers
- `multiply(a, b)` - Multiply two numbers
- `divide(a, b)` - Divide two numbers

### Advanced Operations
- `power(base, exponent)` - Raise base to the power of exponent
- `square_root(x)` - Calculate square root
- `modulo(a, b)` - Calculate modulo (remainder)
- `factorial(n)` - Calculate factorial
- `absolute(x)` - Return absolute value
- `logarithm(x, base)` - Calculate logarithm

### Calculator Class
A stateful `Calculator` class that maintains a running result and operation history:
```python
from calculator import Calculator

calc = Calculator()
calc.add(10)
calc.subtract(3)
calc.multiply(2)
print(calc.get_result())  # 14
```

### Mathematical Utilities
The `math_utils` module provides statistical and mathematical functions:
- `mean(numbers)` - Calculate mean
- `median(numbers)` - Calculate median
- `mode(numbers)` - Calculate mode
- `standard_deviation(numbers)` - Calculate standard deviation
- `gcd(a, b)` - Greatest common divisor
- `lcm(a, b)` - Least common multiple
- `is_prime(n)` - Check if number is prime
- `fibonacci(n)` - Calculate nth Fibonacci number
- `percentage(part, whole)` - Calculate percentage
- `percentage_of(percent, number)` - Calculate percentage of

### Input Validation
The `validators` module provides input validation utilities:
- `validate_number(value)` - Validate number type
- `validate_positive(value)` - Validate positive number
- `validate_non_negative(value)` - Validate non-negative number
- `validate_integer(value)` - Validate integer
- `validate_non_zero(value)` - Validate non-zero
- `validate_range(value, min, max)` - Validate range

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Python API

```python
from calculator import add, subtract, multiply, divide
from calculator import Calculator
from math_utils import mean, median

# Basic operations
result = add(5, 3)  # 8

# Calculator class
calc = Calculator()
calc.add(10)
calc.multiply(2)
print(calc.get_result())  # 20

# Math utilities
avg = mean([1, 2, 3, 4, 5])  # 3.0
```

### Command Line Interface

Interactive mode:
```bash
python cli.py --interactive
```

Single operation:
```bash
python cli.py --operation add --operands 5 3
python cli.py --operation pow --operands 2 8
python cli.py --operation sqrt --operands 16
```

## Testing

Run all tests:
```bash
pytest
```

Run specific test file:
```bash
pytest test_calculator.py
pytest test_advanced.py
pytest test_validators.py
```

## F2P Testing

This project demonstrates F2P (Fail-to-Pass) testing methodology. The `subtract` function had a bug that was fixed, and the test suite includes tests that:
- **F2P Tests**: Failed on the buggy version, pass on the fixed version
- **P2P Tests**: Pass on both versions (regression tests)

See `F2P_DEMO_RESULTS.md` for detailed F2P analysis.

## Project Structure

```
.
├── calculator.py          # Basic and advanced calculator operations
├── math_utils.py          # Mathematical utility functions
├── validators.py          # Input validation utilities
├── cli.py                 # Command-line interface
├── test_calculator.py     # Tests for basic operations
├── test_advanced.py       # Tests for advanced operations
├── test_validators.py     # Tests for validators
├── setup.py              # Package setup
├── pyproject.toml        # Modern Python project configuration
├── requirements.txt      # Production dependencies
└── README.md             # This file
```
