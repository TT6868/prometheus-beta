import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True

def test_palindrome_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("race a car") == False

def test_case_insensitive():
    assert is_palindrome("Racecar") == True
    assert is_palindrome("Hannah") == True

def test_punctuation_and_spaces():
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("hello world") == False

def test_empty_and_single_char():
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_non_string_input():
    with pytest.raises(AttributeError):
        is_palindrome(12321)
    with pytest.raises(AttributeError):
        is_palindrome(None)