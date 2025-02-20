def is_palindrome(input_string: str) -> bool:
    """
    Check if the input string is a palindrome.
    
    Args:
        input_string (str): The string to check for palindrome property.
    
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    
    Notes:
        - The function is case-sensitive
        - Considers special characters and numbers
        - An empty string is considered a palindrome
    """
    # If the string is empty, it's a palindrome
    if not input_string:
        return True
    
    # Compare the string from both ends moving inwards
    left = 0
    right = len(input_string) - 1
    
    while left < right:
        if input_string[left] != input_string[right]:
            return False
        left += 1
        right -= 1
    
    return True