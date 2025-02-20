def has_arithmetic_progression(arr):
    """
    Determines if any three consecutive numbers in the array form an arithmetic progression.
    
    An arithmetic progression is a sequence of numbers where the difference between 
    the consecutive terms is constant.
    
    Args:
        arr (list): A list of positive integers
    
    Returns:
        bool: True if any three consecutive numbers form an arithmetic progression, False otherwise
    
    Raises:
        ValueError: If the input is not a list or contains non-positive integers
    """
    # Validate input
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")
    
    if not all(isinstance(x, int) and x > 0 for x in arr):
        raise ValueError("All elements must be positive integers")
    
    # If array has less than 3 elements, can't form arithmetic progression
    if len(arr) < 3:
        return False
    
    # Check each set of 3 consecutive numbers
    for i in range(len(arr) - 2):
        # Check if the difference between first two and last two numbers is consistent
        if (arr[i+1] - arr[i]) == (arr[i+2] - arr[i+1]):
            return True
    
    return False