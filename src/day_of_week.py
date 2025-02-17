from datetime import datetime

def get_day_of_week(date_input):
    """
    Return the name of the day for a given date.
    
    Args:
        date_input (str or datetime): The date to find the day name for.
                                      Accepts date strings in 'YYYY-MM-DD' format 
                                      or datetime objects.
    
    Returns:
        str: The name of the day (e.g., 'Monday', 'Tuesday', etc.)
    
    Raises:
        ValueError: If the input is not a valid date format
    """
    # If input is a string, convert to datetime
    if isinstance(date_input, str):
        try:
            # Try parsing the date string
            date_obj = datetime.strptime(date_input, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'")
    elif isinstance(date_input, datetime):
        date_obj = date_input
    else:
        raise ValueError("Input must be a date string or datetime object")
    
    # Get the day name and return it
    return date_obj.strftime('%A')