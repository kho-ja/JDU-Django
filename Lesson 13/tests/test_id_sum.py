"""
Test file for student ID digit sum function.
Topshiriq 3: Talaba ID raqamlarini yig'indisini hisoblash.
Misol: ID = 231323, sum = 2+3+1+3+2+3 = 14
"""

import pytest


def calculate_id_sum(student_id):
    """
    Calculate sum of digits in student ID.

    Args:
        student_id: Student ID as integer or string

    Returns:
        int: Sum of all digits in the ID

    Examples:
        >>> calculate_id_sum(231323)
        14
        >>> calculate_id_sum("231323")
        14
        >>> calculate_id_sum(12345)
        15
    """
    # Convert to string to iterate over digits
    id_str = str(student_id)
    # Sum all numeric digits
    return sum(int(digit) for digit in id_str if digit.isdigit())


@pytest.mark.unit
class TestStudentIDSum:
    """Test cases for calculate_id_sum function"""

    def test_id_sum_example_case(self):
        """Test the example case from requirement: 231323 = 14"""
        result = calculate_id_sum(231323)
        assert result == 14

    def test_id_sum_as_string(self):
        """Test ID provided as string"""
        result = calculate_id_sum("231323")
        assert result == 14

    def test_id_sum_as_integer(self):
        """Test ID provided as integer"""
        result = calculate_id_sum(231323)
        assert result == 14

    def test_id_sum_simple_case(self):
        """Test simple sequential ID"""
        result = calculate_id_sum(12345)
        assert result == 1 + 2 + 3 + 4 + 5  # = 15

    def test_id_sum_all_zeros(self):
        """Test ID with all zeros"""
        result = calculate_id_sum(0)
        assert result == 0

    def test_id_sum_all_nines(self):
        """Test ID with all nines"""
        result = calculate_id_sum(999)
        assert result == 27

    def test_id_sum_single_digit(self):
        """Test single digit ID"""
        result = calculate_id_sum(5)
        assert result == 5

    def test_id_sum_with_zeros(self):
        """Test ID containing zeros"""
        result = calculate_id_sum(102030)
        assert result == 6  # 1 + 0 + 2 + 0 + 3 + 0

    def test_id_sum_large_id(self):
        """Test large student ID"""
        result = calculate_id_sum(123456789)
        assert result == 45  # 1+2+3+4+5+6+7+8+9

    def test_id_sum_return_type(self):
        """Test that result is always an integer"""
        result = calculate_id_sum(231323)
        assert isinstance(result, int)


# Parametrized tests for multiple IDs
@pytest.mark.unit
@pytest.mark.parametrize(
    "student_id, expected_sum",
    [
        (231323, 14),  # Example from requirement
        (12345, 15),  # 1+2+3+4+5
        (100000, 1),  # 1+0+0+0+0+0
        (999999, 54),  # 9*6
        (111111, 6),  # 1*6
        (123456, 21),  # 1+2+3+4+5+6
        (0, 0),  # Zero
        (5, 5),  # Single digit
        (10, 1),  # 1+0
        (99, 18),  # 9+9
        ("231323", 14),  # String input
        ("100200", 3),  # String with zeros
    ],
)
def test_id_sum_parametrized(student_id, expected_sum):
    """Parametrized test for multiple student IDs"""
    assert calculate_id_sum(student_id) == expected_sum


@pytest.mark.unit
class TestIDSumProperties:
    """Test mathematical properties of ID sum"""

    def test_id_sum_always_non_negative(self):
        """Test that sum is always non-negative"""
        ids = [123, 456, 789, 0, 1, 999999]
        for id_num in ids:
            result = calculate_id_sum(id_num)
            assert result >= 0

    def test_id_sum_max_single_digit(self):
        """Test that for single digit, sum equals the digit"""
        for digit in range(10):
            result = calculate_id_sum(digit)
            assert result == digit

    def test_id_sum_doubles(self):
        """Test IDs with repeated digits"""
        result = calculate_id_sum(222222)
        assert result == 12  # 2*6

        result = calculate_id_sum(555)
        assert result == 15  # 5*3

    def test_id_sum_ascending(self):
        """Test ascending digit sequence"""
        result = calculate_id_sum(123456789)
        assert result == 45

    def test_id_sum_descending(self):
        """Test descending digit sequence"""
        result = calculate_id_sum(987654321)
        assert result == 45  # Same as ascending


# Real-world student ID examples
@pytest.mark.unit
class TestRealWorldIDs:
    """Test with realistic student ID formats"""

    def test_typical_6_digit_id(self):
        """Test typical 6-digit student ID"""
        result = calculate_id_sum(231323)
        assert result == 14

    def test_typical_5_digit_id(self):
        """Test 5-digit student ID"""
        result = calculate_id_sum(12345)
        assert result == 15

    def test_year_based_id(self):
        """Test ID starting with year (2024...)"""
        result = calculate_id_sum(202401)
        assert result == 9  # 2+0+2+4+0+1

    def test_sequential_ids(self):
        """Test sequential student IDs"""
        id1 = calculate_id_sum(231323)
        id2 = calculate_id_sum(231324)
        # Second ID sum should be 1 more (3 becomes 4)
        assert id2 == id1 + 1


# Edge cases
@pytest.mark.unit
class TestIDSumEdgeCases:
    """Edge case tests for calculate_id_sum"""

    def test_id_sum_very_large_number(self):
        """Test very large ID number"""
        result = calculate_id_sum(9999999999)
        assert result == 90  # 9*10

    def test_id_sum_leading_zeros_as_string(self):
        """Test string ID with leading zeros"""
        result = calculate_id_sum("001234")
        assert result == 10  # 0+0+1+2+3+4

    def test_id_sum_consistency(self):
        """Test that same ID always gives same result"""
        id_num = 231323
        results = [calculate_id_sum(id_num) for _ in range(10)]
        assert len(set(results)) == 1  # All results should be the same
        assert results[0] == 14
