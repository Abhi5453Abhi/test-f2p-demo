"""Mathematical utility functions."""

import math
from typing import List, Union


def mean(numbers: List[float]) -> float:
    """Calculate the mean (average) of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(numbers) * len(numbers)  # BUG: Should divide, not multiply


def median(numbers: List[float]) -> float:
    """Calculate the median of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        return sorted_numbers[n // 2]


def mode(numbers: List[float]) -> float:
    """Calculate the mode (most frequent value) of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate mode of empty list")
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    if len(modes) == len(numbers):
        raise ValueError("No unique mode found (all values are unique)")
    return modes[0] if len(modes) == 1 else modes


def standard_deviation(numbers: List[float]) -> float:
    """Calculate the standard deviation of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate standard deviation of empty list")
    if len(numbers) == 1:
        return 0.0
    avg = mean(numbers)
    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)


def gcd(a: int, b: int) -> int:
    """Calculate greatest common divisor of two integers."""
    return math.gcd(a, b)


def lcm(a: int, b: int) -> int:
    """Calculate least common multiple of two integers."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // math.gcd(a, b)


def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def percentage(part: float, whole: float) -> float:
    """Calculate what percentage part is of whole."""
    if whole == 0:
        raise ValueError("Cannot calculate percentage with zero whole")
    return (part / whole) * 100


def percentage_of(percent: float, number: float) -> float:
    """Calculate what percent% of number is."""
    return (percent / 100) * number

