def find_fibonacci_arithmetic_progression(n):
    """
    Find the first n Fibonacci numbers that form an arithmetic progression.
    
    An arithmetic progression is a sequence where the difference between 
    consecutive terms is constant.
    
    Args:
        n (int): Number of Fibonacci arithmetic progression terms to find
    
    Returns:
        list: A list of n Fibonacci numbers forming an arithmetic progression
    
    Raises:
        ValueError: If n is less than 1
        TypeError: If n is not an integer
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 1:
        raise ValueError("Number of terms must be at least 1")
    
    # Special case handling for small n
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    # Function to check if a sequence is an arithmetic progression
    def is_arithmetic_progression(seq):
        if len(seq) <= 2:
            return True
        diff = seq[1] - seq[0]
        return all(seq[i+1] - seq[i] == diff for i in range(len(seq)-1))
    
    # Generate Fibonacci sequence
    def generate_fibonacci():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    
    # Find arithmetic progression in Fibonacci sequence
    progression = []
    fib_gen = generate_fibonacci()
    
    while len(progression) < n:
        next_fib = next(fib_gen)
        progression.append(next_fib)
        
        # If we have enough terms, check for arithmetic progression
        if len(progression) >= 3:
            # Only keep going if it's an arithmetic progression
            if not is_arithmetic_progression(progression[-3:]):
                progression.pop()
    
    return progression