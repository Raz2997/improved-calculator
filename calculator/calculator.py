# calculator/calculator.py

class Calculator:
    """A simple calculator class that can perform basic arithmetic operations."""

    @staticmethod
    def add(a: float, b: float) -> float:
        """Returns the sum of a and b."""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Returns the difference of a and b."""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Returns the product of a and b."""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Returns the quotient of a divided by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
