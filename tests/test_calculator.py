# tests/test_calculator.py
import pytest
from calculator.calculator import Calculator  # Corrected import path

# Create a fixture to set up the calculator object
@pytest.fixture
def calc():
    return Calculator()

# Test addition
def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(1, 1) == 2
    assert calc.add(0, 0) == 0

# Test subtraction
def test_subtract(calc):
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(5, 5) == 0
    assert calc.subtract(0, 0) == 0

# Test multiplication
def test_multiply(calc):
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0, 5) == 0

# Test division
def test_divide(calc):
    assert calc.divide(10, 5) == 2
    assert calc.divide(9, 3) == 3
    with pytest.raises(ValueError):
        calc.divide(10, 0)  # Should raise an exception for division by zero
