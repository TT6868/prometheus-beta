import pytest
from src.prime_pair_sum import prime_pair_sum, is_prime

def test_prime_pair_sum_basic():
    """Test basic functionality with a small input."""
    assert prime_pair_sum(10) == [5, 7, 11, 13]

def test_prime_pair_sum_edge_cases():
    """Test edge cases with minimal and invalid inputs."""
    assert prime_pair_sum(1) == []
    assert prime_pair_sum(2) == []
    assert prime_pair_sum(0) == []
    assert prime_pair_sum(-5) == []

def test_prime_pair_sum_larger_input():
    """Test with a larger input."""
    result = prime_pair_sum(20)
    assert len(result) > 0
    # Verify all numbers in result are prime
    assert all(is_prime(num) for num in result)
    # Verify numbers are unique and sorted
    assert result == sorted(set(result))

def test_is_prime():
    """Test the is_prime helper function."""
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(17) == True
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(-5) == False