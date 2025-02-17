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
    
    # Formatting preparation
    if is_nested:
        # Ensure uniform length nested list
        max_len = max(len(item) if isinstance(item, (list, dict)) else 1 for item in arr)
        formatted_arr = [list(item) if isinstance(item, (list, dict)) else [item] + [None] * (max_len - 1) for item in arr]
    else:
        # For flat lists, add index column
        formatted_arr = list(enumerate(arr))
        
    # Header handling
    if headers is None:
        if is_nested:
            # Use range for nested data
            headers = list(range(len(formatted_arr[0])))
        else:
            # Use predefined headers for flat lists
            headers = ['Index', 'Value']
    
    # Validate headers
    if len(headers) != len(formatted_arr[0]):
        raise ValueError("Headers length must match data structure")
    
    # Convert everything to string
    str_formatted_arr = [[str(item) if item is not None else '' for item in row] for row in formatted_arr]
    
    # Calculate column widths (including headers)
    col_widths = [
        max(len(str(header)), max(len(row[i]) for row in str_formatted_arr)) 
        for i, header in enumerate(headers)
    ]
    
    # Create table format
    def format_row(row):
        return " | ".join(f"{str(item):<{width}}" for item, width in zip(row, col_widths))
    
    # Construct table
    table_lines = [
        format_row(headers),  # Header row
        "-" * (sum(col_widths) + 3 * (len(col_widths) - 1))  # Separator
    ]
    table_lines.extend(format_row(row) for row in str_formatted_arr)
    
    return "\n".join(table_lines)