import os
import platform
from datetime import datetime

def get_file_creation_date(file_path):
    """
    Get the creation date of a file across different platforms.
    
    Args:
        file_path (str): Path to the file
    
    Returns:
        datetime: Creation date of the file
    
    Raises:
        FileNotFoundError: If the file does not exist
        PermissionError: If there's no permission to access the file
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        # Windows
        if platform.system() == 'Windows':
            return datetime.fromtimestamp(os.path.getctime(file_path))
        
        # macOS
        elif platform.system() == 'Darwin':
            stat = os.stat(file_path)
            return datetime.fromtimestamp(stat.st_birthtime)
        
        # Linux and other Unix-like systems
        else:
            stat = os.stat(file_path)
            # Use creation time if available, otherwise use metadata change time
            creation_time = getattr(stat, 'st_birthtime', stat.st_ctime)
            return datetime.fromtimestamp(creation_time)
    
    except PermissionError:
        raise PermissionError(f"Permission denied to access file: {file_path}")
    except Exception as e:
        raise OSError(f"Error getting file creation date: {str(e)}")