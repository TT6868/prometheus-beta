import pytest
from src.replace_spaces import replace_spaces_with_underscores

def test_replace_spaces_normal_string():
    """Test replacing spaces in a normal string."""
    input_str = "hello world python"
    assert replace_spaces_with_underscores(input_str) == "hello_world_python"

def test_replace_spaces_multiple_consecutive_spaces():
    """Test replacing multiple consecutive spaces."""
    input_str = "hello   world  python"
    assert replace_spaces_with_underscores(input_str) == "hello___world__python"

def test_replace_spaces_empty_string():
    """Test with an empty string."""
    input_str = ""
    assert replace_spaces_with_underscores(input_str) == ""

def test_replace_spaces_no_spaces():
    """Test a string with no spaces."""
    input_str = "helloworld"
    assert replace_spaces_with_underscores(input_str) == "helloworld"

def test_replace_spaces_leading_trailing_spaces():
    """Test a string with leading and trailing spaces."""
    input_str = "  hello world  "
    assert replace_spaces_with_underscores(input_str) == "__hello_world__"

def test_replace_spaces_invalid_input():
    """Test raising TypeError for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_spaces_with_underscores(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_spaces_with_underscores(None)