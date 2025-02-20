import pytest
from src.arithmetic_progression import has_arithmetic_progression

def test_has_arithmetic_progression_standard_case():
    # Test a case where an arithmetic progression exists
    assert has_arithmetic_progression([1, 3, 5, 7, 9]) == True
    assert has_arithmetic_progression([2, 4, 6, 8, 10]) == True
    assert has_arithmetic_progression([3, 5, 7, 9, 11]) == True

def test_has_arithmetic_progression_no_progression():
    # Test cases where no arithmetic progression exists
    assert has_arithmetic_progression([1, 2, 4, 8, 16]) == False
    assert has_arithmetic_progression([1, 3, 6, 10, 15]) == False
    assert has_arithmetic_progression([1, 2, 3, 5, 8]) == False

def test_has_arithmetic_progression_edge_cases():
    # Test edge cases
    assert has_arithmetic_progression([1, 1, 1]) == True  # constant sequence
    assert has_arithmetic_progression([1, 2, 3]) == True  # minimum length with progression
    assert has_arithmetic_progression([1, 2]) == False    # too short
    assert has_arithmetic_progression([]) == False        # empty list

def test_has_arithmetic_progression_invalid_input():
    # Test invalid input raises ValueError
    with pytest.raises(ValueError, match="Input must be a list"):
        has_arithmetic_progression(123)
    
    with pytest.raises(ValueError, match="All elements must be positive integers"):
        has_arithmetic_progression([1, 2, -3])
    
    with pytest.raises(ValueError, match="All elements must be positive integers"):
        has_arithmetic_progression([1, 2, 3.5])