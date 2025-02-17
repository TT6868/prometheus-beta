import os
import pytest
from src.file_utils import check_file_exists

def test_check_file_exists_existing_files():
    # Test existing files in the repository
    assert check_file_exists('.gitignore') == True
    assert check_file_exists('README.md') == True
    assert check_file_exists('requirements.txt') == True

def test_check_file_exists_nonexistent_file():
    # Test nonexistent file
    assert check_file_exists('nonexistent_file.txt') == False

def test_check_file_exists_empty_path():
    # Test empty path
    assert check_file_exists('') == False

def test_check_file_exists_none_path():
    # Test None path raises TypeError
    with pytest.raises(TypeError):
        check_file_exists(None)

def test_check_file_exists_directory():
    # Ensure it returns False for directories
    assert check_file_exists('.') == False
    assert check_file_exists('src') == False