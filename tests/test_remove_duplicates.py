import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    # Test basic case with duplicates
    assert remove_duplicates([1, 1, 2, 3, 3, 4, 5, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_empty_list():
    # Test empty list
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    # Test list with no duplicates
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_all_same():
    # Test list with all same elements
    assert remove_duplicates([2, 2, 2, 2]) == [2]

def test_remove_duplicates_none_input():
    # Test None input
    assert remove_duplicates(None) == []

def test_remove_duplicates_negative_numbers():
    # Test with negative numbers
    assert remove_duplicates([-3, -3, -2, -1, -1, 0, 0, 1, 1]) == [-3, -2, -1, 0, 1]