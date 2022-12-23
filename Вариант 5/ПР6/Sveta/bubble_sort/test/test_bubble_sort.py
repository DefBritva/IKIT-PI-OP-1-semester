import pytest

from bubble_sort import bubble_sort


def test_bubble_sort():
    """
    test is algorythm working correctly
    """
    test_arr = [5, 2, 3, 1]
    expected = [1, 2, 3, 5]

    result = bubble_sort.sort(test_arr)
    assert result == expected


if __name__ == "__main__":
    pytest.main()
