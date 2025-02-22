import os

def get_file_extension(file_path):
    """
    Get the file extension from a given file path.
    
    Args:
        file_path (str): The path to the file.
    
    Returns:
        str: The file extension (without the dot), or an empty string if no extension.
    """
    # Get the base file name with extension from the path
    filename = os.path.basename(file_path)
    
    # Split the filename and get the extension 
    # splitext returns (root, ext) where ext includes the dot
    return os.path.splitext(filename)[1][1:]  # Remove the leading dot