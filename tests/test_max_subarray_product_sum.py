import pytest
from src.max_subarray_product_sum import find_max_subarray_product_sum

def test_basic_scenario():
    """Test a basic scenario with a simple input"""
    arr = [2, 3, 4, 5, 6]
    target_product = 120
    assert find_max_subarray_product_sum(arr, target_product) == 15

def test_multiple_valid_subarrays():
    """Test when multiple subarrays have the target product"""
    arr = [1, 2, 3, 4, 5]
    target_product = 24
    assert find_max_subarray_product_sum(arr, target_product) == 12  # 3 + 4 = 7

def test_first_subarray():
    """Test the first subarray matching the target product"""
    arr = [1, 2, 3, 4, 5]
    target_product = 6
    assert find_max_subarray_product_sum(arr, target_product) == 5  # 2 + 3

def test_no_matching_subarray():
    """Test when no subarray matches the target product"""
    arr = [1, 2, 3, 4, 5]
    target_product = 1000
    assert find_max_subarray_product_sum(arr, target_product) == -1

def test_single_element_match():
    """Test when a single element matches the target product"""
    arr = [1, 2, 3, 4, 5]
    target_product = 3
    assert find_max_subarray_product_sum(arr, target_product) == 3

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Empty array
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_max_subarray_product_sum([], 10)
    
    # Non-positive integers
    with pytest.raises(ValueError, match="All array elements must be positive integers"):
        find_max_subarray_product_sum([1, 2, -3, 4], 10)
        
def test_large_input():
    """Test with a larger input to ensure performance"""
    arr = list(range(1, 11))  # [1, 2, 3, ..., 10]
    target_product = 120  # 1 * 2 * 3 * 4 * 5
    assert find_max_subarray_product_sum(arr, target_product) == 15  # 1 + 2 + 3 + 4 + 5