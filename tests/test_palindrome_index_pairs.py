import pytest
from src.palindrome_index_pairs import find_palindrome_index_pairs

def test_palindrome_index_pairs_basic():
    words = ["bat", "tab", "cat"]
    result = find_palindrome_index_pairs(words)
    assert [0, 1] in result and [1, 0] in result
    assert len(result) == 2

def test_palindrome_index_pairs_empty_list():
    words = []
    result = find_palindrome_index_pairs(words)
    assert result == []

def test_palindrome_index_pairs_single_word():
    words = ["hello"]
    result = find_palindrome_index_pairs(words)
    assert result == []

def test_palindrome_index_pairs_complex_case():
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    result = find_palindrome_index_pairs(words)
    expected = [[0, 1], [1, 0], [2, 4], [3, 2]]
    for pair in expected:
        assert pair in result

def test_palindrome_index_pairs_no_matches():
    words = ["apple", "banana", "cherry"]
    result = find_palindrome_index_pairs(words)
    assert result == []