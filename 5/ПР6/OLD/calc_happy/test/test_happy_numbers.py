#!/usr/bin/env python
"""
test code for calc_happy module
"""

import pytest

from calc_happy import calc_happy_numbers
from calc_happy.calc_happy_numbers import is_happy_number


def test_is_happy_number():
    """
    test is every single numbers calculating correctly
    """
    test_numbers = [7, 15, 19]
    expected = [True, False, True]

    result = [is_happy_number(i)[0] for i in test_numbers]
    assert result == expected


def test_calc_happy_numbers():
    """
    test is algorythm working correctly
    """
    test_number = 20
    expected = [1, 7, 10, 13, 19]

    result = calc_happy_numbers.calculate_happy_numbers(test_number)
    assert result == expected


if __name__ == "__main__":
    pytest.main()
