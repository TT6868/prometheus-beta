def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_pair_sum(n):
    """
    Returns a list of unique prime numbers that can be obtained 
    by summing pairs of numbers from the range [1, n].
    
    Args:
        n (int): The upper limit of the range.
    
    Returns:
        list: Sorted list of unique prime numbers obtained by pair-wise summation.
    """
    # Validate input
    if not isinstance(n, int) or n < 2:
        return []
    
    # Generate all possible pair sums
    pair_sums = set()
    for i in range(1, n):
        for j in range(i, n + 1):
            pair_sum = i + j
            if pair_sum <= n * 2:  # Limit sum to reasonable range
                pair_sums.add(pair_sum)
    
    # Filter prime numbers
    prime_sums = sorted(num for num in pair_sums if is_prime(num))
    
    return prime_sums