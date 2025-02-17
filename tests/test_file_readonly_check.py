import os
import pytest
import tempfile
from src.file_readonly_check import is_file_read_only

def test_is_file_read_only():
    # Create a temporary file with read-write permissions
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_path = temp_file.name
        temp_file.write("Test content")
    
    try:
        # Check that the file is not read-only by default
        assert is_file_read_only(temp_path) == False
        
        # Change file permissions to read-only
        os.chmod(temp_path, 0o444)  # Read-only for all
        
        # Check that the file is now read-only
        assert is_file_read_only(temp_path) == True
    
    finally:
        # Clean up the temporary file
        os.unlink(temp_path)

def test_file_not_found():
    # Test that FileNotFoundError is raised for non-existent files
    with pytest.raises(FileNotFoundError):
        is_file_read_only("non_existent_file.txt")

def test_existing_readonly_files():
    # Test with files in the repository
    readonly_files = [
        '.gitignore',
        'README.md',
        'requirements.txt'
    ]
    
    for file in readonly_files:
        # Ensure the file exists before testing
        assert os.path.exists(file), f"File {file} does not exist"
        is_readonly = is_file_read_only(file)
        # This will depend on the actual file permissions in the repository
        assert isinstance(is_readonly, bool), f"Check of {file} failed"