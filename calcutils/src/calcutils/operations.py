"""
operations.py
Core arithmetic and statistical helper functions for calcutils.
"""

def add(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b

def multiply(a: float, b: float) -> float:
    """Returns the product of two numbers."""
    return a * b

def average(numbers: list) -> float:
    """Returns the arithmetic mean of a list of numbers."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers"""
    if b == 0:
        raise ValueError("Division by zero is not possible")
    return a / b
    
def subtract(a: float, b: float) -> float:
    """Return the difference between two numbers."""
    return a - b

