def remove_duplicates(sorted_list):
    """
    Remove duplicate values from a sorted list of integers.
    
    Args:
        sorted_list (list): A sorted list of integers
    
    Returns:
        list: A new list with duplicate values removed
    """
    # Handle empty or None input
    if not sorted_list:
        return []
    
    # Initialize result list with first element
    result = [sorted_list[0]]
    
    # Iterate through the rest of the list
    for num in sorted_list[1:]:
        # Only add number if it's different from the last added number
        if num != result[-1]:
            result.append(num)
    
    return result