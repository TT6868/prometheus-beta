import os
import pytest
import tempfile
from datetime import datetime, timedelta
from src.file_creation_date import get_file_creation_date

def test_get_file_creation_date():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        # Get current time before file creation
        before_creation = datetime.now()
        
        # Wait for a moment to ensure distinct timestamp
        import time
        time.sleep(0.1)
        
        # Get the file's creation date
        creation_date = get_file_creation_date(temp_path)
        
        # Assertions
        assert isinstance(creation_date, datetime)
        assert before_creation <= creation_date <= datetime.now()
    
    finally:
        # Clean up the temporary file
        os.unlink(temp_path)

def test_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        get_file_creation_date("/path/to/nonexistent/file.txt")

def test_permission_denied(mocker):
    # Mock os.path.exists to return True
    mocker.patch('os.path.exists', return_value=True)
    
    # Mock os.stat to raise PermissionError
    mocker.patch('os.stat', side_effect=PermissionError)
    
    with pytest.raises(PermissionError):
        get_file_creation_date("/some/restricted/file.txt")

def test_return_type():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        creation_date = get_file_creation_date(temp_path)
        assert isinstance(creation_date, datetime)
    
    finally:
        # Clean up the temporary file
        os.unlink(temp_path)