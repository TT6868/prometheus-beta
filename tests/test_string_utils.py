import pytest
from src.string_utils import count_words

def test_count_words_default_separator():
    """Test word counting with default space separator."""
    assert count_words("hello world python") == 3
    assert count_words("  hello   world  python  ") == 3

def test_count_words_custom_separator():
    """Test word counting with custom separator."""
    assert count_words("apple,banana,cherry", separator=",") == 3
    assert count_words("one::two::three", separator="::") == 3

def test_count_words_empty_string():
    """Test word counting with empty string."""
    assert count_words("") == 0
    assert count_words("", separator=",") == 0

def test_count_words_no_separator_match():
    """Test word counting when separator is not in string."""
    assert count_words("hello", separator=",") == 1

def test_count_words_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Input must be a string"):
        count_words(123)
    
    with pytest.raises(TypeError, match="Separator must be a string"):
        count_words("hello", separator=123)

def test_count_words_consecutive_separators():
    """Test handling of consecutive separators."""
    assert count_words("apple,,banana,,cherry", separator=",,") == 3