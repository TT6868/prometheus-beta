def find_max(arr):
    """
    Find the maximum number in an array.
    
    Args:
        arr (list): A list of numbers
    
    Returns:
        int or float: The maximum number in the array
    
    Raises:
        ValueError: If the input array is empty
    """
    if not arr:
        raise ValueError("Cannot find maximum of an empty array")
    
    return max(arr)