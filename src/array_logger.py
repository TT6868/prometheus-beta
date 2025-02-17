def log_array_as_table(arr, headers=None):
    """
    Log an array in a formatted table.
    
    Args:
        arr (list): The array to be logged.
        headers (list, optional): Column headers for the table. 
                                  Defaults to None.
    
    Returns:
        str: A formatted table representation of the array.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If headers length doesn't match array item length.
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        return "Empty array"
    
    # Determine if we're dealing with nested lists/dicts or flat lists
    is_nested = any(isinstance(item, (list, dict)) for item in arr)
    
    # Convert all items to strings for consistent formatting
    if is_nested:
        # For nested structures, convert to string representation
        formatted_arr = [str(item) for item in arr]
    else:
        # For flat lists, keep as-is
        formatted_arr = arr
    
    # Header handling
    if headers is None:
        if is_nested:
            # If no headers provided for nested data, use indices
            headers = list(range(len(formatted_arr[0]) if formatted_arr else 0))
        else:
            # For flat lists, use index as header
            headers = ['Index', 'Value']
            formatted_arr = list(enumerate(formatted_arr))
    elif len(headers) != (len(formatted_arr[0]) if is_nested else 2):
        raise ValueError("Headers length must match data structure")
    
    # Calculate column widths
    col_widths = [max(len(str(item)) for item in col) for col in zip(*formatted_arr, headers)]
    
    # Create table format
    def format_row(row):
        return " | ".join(f"{str(item):<{width}}" for item, width in zip(row, col_widths))
    
    # Construct table
    table_lines = [
        format_row(headers),  # Header row
        "-" * (sum(col_widths) + 3 * (len(col_widths) - 1))  # Separator
    ]
    table_lines.extend(format_row(row) for row in formatted_arr)
    
    return "\n".join(table_lines)