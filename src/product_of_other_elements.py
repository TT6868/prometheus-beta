def product_of_other_elements(nums):
    """
    Returns a list where each element is the product of all other elements except itself.
    
    Args:
        nums (list): A list of integers or floats
    
    Returns:
        list: A list where each element is the product of all other elements
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-numeric elements
    """
    # Check input type
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    # Check that all elements are numeric
    if not all(isinstance(x, (int, float)) for x in nums):
        raise ValueError("All elements must be numeric")
    
    # Handle empty list or list with fewer than 2 elements
    if len(nums) < 2:
        return []
    
    # Calculate total product
    total_product = 1
    for num in nums:
        total_product *= num
    
    # Create result list by dividing total product by each element
    result = []
    for num in nums:
        # Avoid division by zero
        if num == 0:
            # If current element is zero, product is product of all other non-zero elements
            non_zero_product = 1
            for other in nums:
                if other != 0:
                    non_zero_product *= other
            result.append(non_zero_product)
        else:
            result.append(total_product / num)
    
    return result