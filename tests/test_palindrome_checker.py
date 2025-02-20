import pytest
from src.palindrome_checker import is_palindrome

def test_palindrome_basic():
    # Basic palindromes
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    
def test_palindrome_case_sensitivity():
    # Case-sensitive checks
    assert is_palindrome("Racecar") == False
    assert is_palindrome("RaceCar") == False
    
def test_palindrome_with_special_chars():
    # Palindromes with special characters and numbers
    assert is_palindrome("A man, a plan, a canal: Panama") == False
    assert is_palindrome("race a car") == False
    
def test_palindrome_numbers():
    # Numeric palindromes
    assert is_palindrome("12321") == True
    assert is_palindrome("123") == False
    
def test_empty_and_single_char():
    # Empty string and single character
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    
def test_non_palindromes():
    # Non-palindrome strings
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    
def test_mixed_palindrome():
    # Mixed palindromes with various characters
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A1b22c1a") == False