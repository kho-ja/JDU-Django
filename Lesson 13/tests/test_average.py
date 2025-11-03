"""
Test file for average calculation function.
Topshiriq 2: Sodda ikkita sonning o'rta arifmetikini hisoblash.
"""

import pytest


def calculate_average(a, b):
    """
    Calculate arithmetic mean (average) of two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        float: Average of the two numbers

    Examples:
        >>> calculate_average(4, 6)
        5.0
        >>> calculate_average(10, 20)
        15.0
    """
    return (a + b) / 2


@pytest.mark.unit
class TestAverageFunction:
    """Test cases for calculate_average function"""

    def test_average_positive_integers(self):
        """Test average of two positive integers"""
        result = calculate_average(4, 6)
        assert result == 5.0

    def test_average_equal_numbers(self):
        """Test average when both numbers are equal"""
        result = calculate_average(10, 10)
        assert result == 10.0

    def test_average_negative_numbers(self):
        """Test average of two negative numbers"""
        result = calculate_average(-5, -15)
        assert result == -10.0

    def test_average_positive_and_negative(self):
        """Test average of one positive and one negative number"""
        result = calculate_average(10, -10)
        assert result == 0.0

    def test_average_with_zero(self):
        """Test average with zero"""
        result = calculate_average(0, 10)
        assert result == 5.0

    def test_average_float_numbers(self):
        """Test average of float numbers"""
        result = calculate_average(2.5, 7.5)
        assert result == 5.0

    def test_average_large_numbers(self):
        """Test average of large numbers"""
        result = calculate_average(1000, 2000)
        assert result == 1500.0

    def test_average_decimal_result(self):
        """Test when average results in decimal"""
        result = calculate_average(5, 6)
        assert result == 5.5

    def test_average_symmetry(self):
        """Test that order doesn't matter (commutative property)"""
        assert calculate_average(3, 7) == calculate_average(7, 3)

    def test_average_return_type(self):
        """Test that result is always a float"""
        result = calculate_average(4, 6)
        assert isinstance(result, float)


# Parametrized tests for multiple test cases
@pytest.mark.unit
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (0, 0, 0.0),
        (1, 1, 1.0),
        (10, 20, 15.0),
        (100, 200, 150.0),
        (-10, 10, 0.0),
        (2.5, 7.5, 5.0),
        (3, 7, 5.0),
    ],
)
def test_average_parametrized(a, b, expected):
    """Parametrized test for multiple input combinations"""
    assert calculate_average(a, b) == expected


# Edge case tests
@pytest.mark.unit
class TestAverageEdgeCases:
    """Edge case tests for calculate_average function"""

    def test_average_very_small_numbers(self):
        """Test average of very small numbers"""
        result = calculate_average(0.001, 0.002)
        assert round(result, 4) == 0.0015

    def test_average_both_zero(self):
        """Test average when both numbers are zero"""
        result = calculate_average(0, 0)
        assert result == 0.0

    def test_average_same_sign_different_magnitude(self):
        """Test numbers with same sign but different magnitudes"""
        result = calculate_average(1, 99)
        assert result == 50.0
