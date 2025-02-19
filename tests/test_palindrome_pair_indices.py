import pytest
from src.palindrome_pair_indices import find_palindrome_pair_indices

def test_basic_palindrome_pairs():
    """Test basic palindrome pairs scenario."""
    words = ["bat", "tab", "cat"]
    assert find_palindrome_pair_indices(words) == [[0, 1]]

def test_multiple_palindrome_pairs():
    """Test scenario with multiple palindrome pairs."""
    words = ["hello", "olleh", "world", "dlrow"]
    result = find_palindrome_pair_indices(words)
    assert [0, 1] in result and [2, 3] in result

def test_no_palindrome_pairs():
    """Test scenario with no palindrome pairs."""
    words = ["apple", "banana", "cherry"]
    assert find_palindrome_pair_indices(words) == []

def test_single_word_list():
    """Test scenario with a single word."""
    words = ["racecar"]
    assert find_palindrome_pair_indices(words) == []

def test_empty_list():
    """Test scenario with an empty list."""
    words = []
    assert find_palindrome_pair_indices(words) == []