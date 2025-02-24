import pytest
from src.fibonacci_arithmetic import find_fibonacci_arithmetic_progression

def test_basic_functionality():
    """Test basic functionality of the function"""
    result = find_fibonacci_arithmetic_progression(4)
    assert len(result) == 4, "Should return 4 terms"
    
    # Verify it's a Fibonacci sequence
    assert result[2] == result[0] + result[1], "Should be Fibonacci numbers"

def test_single_term():
    """Test when only one term is requested"""
    result = find_fibonacci_arithmetic_progression(1)
    assert result == [0], "Should return [0] for n=1"

def test_two_terms():
    """Test when two terms are requested"""
    result = find_fibonacci_arithmetic_progression(2)
    assert result == [0, 1], "Should return [0, 1] for n=2"

def test_arithmetic_progression():
    """Test that the returned sequence forms an arithmetic progression"""
    result = find_fibonacci_arithmetic_progression(4)
    assert result[1] - result[0] == result[2] - result[1], "Should form an arithmetic progression"

def test_error_handling():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        find_fibonacci_arithmetic_progression("3")
    
    with pytest.raises(ValueError):
        find_fibonacci_arithmetic_progression(0)
    
    with pytest.raises(ValueError):
        find_fibonacci_arithmetic_progression(-1)

def test_longer_sequence():
    """Test a longer sequence to ensure arithmetic progression is maintained"""
    result = find_fibonacci_arithmetic_progression(6)
    assert len(result) == 6, "Should return 6 terms"
    
    # Check arithmetic progression is maintained
    diff = result[1] - result[0]
    for i in range(2, len(result)):
        assert result[i] - result[i-1] == diff, f"Arithmetic progression broken at index {i}"