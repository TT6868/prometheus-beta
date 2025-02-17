def capitalize_words(input_string):
    """
    Capitalizes the first letter of each word in a given string.
    
    Args:
        input_string (str): The input string to capitalize.
    
    Returns:
        str: A string with the first letter of each word capitalized.
    
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Split the string into words, capitalize each word, then join
    return ' '.join(word.capitalize() for word in input_string.split())