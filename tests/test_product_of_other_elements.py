import pytest
from src.product_of_other_elements import product_of_other_elements

def test_normal_case():
    """Test with a standard list of positive integers"""
    assert product_of_other_elements([1, 2, 3, 4]) == [24.0, 12.0, 8.0, 6.0]

def test_with_zeros():
    """Test with a list containing zeros"""
    assert product_of_other_elements([1, 0, 3, 4]) == [0.0, 12.0, 0.0, 0.0]

def test_with_negative_numbers():
    """Test with negative numbers"""
    assert product_of_other_elements([-1, 1, 0, -3, 3]) == [0.0, 0.0, 9.0, 0.0, 0.0]

def test_single_element():
    """Test with a single element"""
    assert product_of_other_elements([5]) == []

def test_empty_list():
    """Test with an empty list"""
    assert product_of_other_elements([]) == []

def test_invalid_input_type():
    """Test with non-list input"""
    with pytest.raises(TypeError):
        product_of_other_elements(123)

def test_non_numeric_elements():
    """Test with non-numeric elements"""
    with pytest.raises(ValueError):
        product_of_other_elements([1, 2, 'a', 4])

def test_floating_point_numbers():
    """Test with floating point numbers"""
    assert product_of_other_elements([1.5, 2.5, 3.5]) == [8.75, 5.25, 3.75]