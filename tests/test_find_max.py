import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.find_max import find_max

def test_find_max_positive_numbers():
    """Test finding max in an array of positive numbers"""
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([10, 20, 30, 40]) == 40

def test_find_max_mixed_numbers():
    """Test finding max in an array with mixed positive and negative numbers"""
    assert find_max([-1, 0, 1, 2]) == 2
    assert find_max([-10, -5, -3]) == -3

def test_find_max_single_element():
    """Test finding max in an array with a single element"""
    assert find_max([42]) == 42

def test_find_max_floating_point():
    """Test finding max in an array with floating point numbers"""
    assert find_max([1.5, 2.7, 0.3, 4.1]) == 4.1

def test_find_max_empty_array():
    """Test that an empty array raises a ValueError"""
    with pytest.raises(ValueError, match="Cannot find maximum of an empty array"):
        find_max([])