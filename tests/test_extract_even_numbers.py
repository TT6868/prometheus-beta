import pytest
from src.extract_even_numbers import extract_even_numbers

def test_extract_even_numbers_standard_case():
    """Test with a list containing both even and odd numbers"""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [2, 4, 6, 8, 10]
    assert extract_even_numbers(input_list) == expected

def test_extract_even_numbers_all_odd():
    """Test with a list containing only odd numbers"""
    input_list = [1, 3, 5, 7, 9]
    expected = []
    assert extract_even_numbers(input_list) == expected

def test_extract_even_numbers_all_even():
    """Test with a list containing only even numbers"""
    input_list = [2, 4, 6, 8, 10]
    expected = [2, 4, 6, 8, 10]
    assert extract_even_numbers(input_list) == expected

def test_extract_even_numbers_empty_list():
    """Test with an empty list"""
    input_list = []
    expected = []
    assert extract_even_numbers(input_list) == expected

def test_extract_even_numbers_negative_numbers():
    """Test with a list containing negative numbers"""
    input_list = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    expected = [-4, -2, 0, 2, 4]
    assert extract_even_numbers(input_list) == expected

def test_extract_even_numbers_preserves_order():
    """Test that the order of even numbers is preserved"""
    input_list = [1, 3, 2, 5, 4, 7, 6, 9, 8]
    expected = [2, 4, 6, 8]
    assert extract_even_numbers(input_list) == expected