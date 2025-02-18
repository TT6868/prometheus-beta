import os
import zipfile
import pytest
import tempfile
import shutil

from src.zip_extractor import extract_zip_files

def create_test_zip(files_dict):
    """Helper function to create a test zip file with given files."""
    temp_zip = tempfile.mktemp(suffix='.zip')
    with zipfile.ZipFile(temp_zip, 'w') as zf:
        for filename, content in files_dict.items():
            zf.writestr(filename, content)
    return temp_zip

def test_extract_zip_files_basic():
    """Test basic zip file extraction."""
    test_files = {
        'file1.txt': 'content1',
        'file2.txt': 'content2'
    }
    
    with tempfile.TemporaryDirectory() as extract_dir:
        zip_path = create_test_zip(test_files)
        
        try:
            extracted_files = extract_zip_files(zip_path, extract_dir)
            
            # Check number of extracted files
            assert len(extracted_files) == len(test_files)
            
            # Check each file was extracted
            for filename in test_files.keys():
                file_path = os.path.join(extract_dir, filename)
                assert os.path.exists(file_path)
                
                # Check file content
                with open(file_path, 'r') as f:
                    assert f.read() == test_files[filename]
        finally:
            os.unlink(zip_path)

def test_extract_zip_files_default_path():
    """Test extraction to default path."""
    test_files = {'test.txt': 'test content'}
    
    with tempfile.TemporaryDirectory() as temp_dir:
        os.chdir(temp_dir)
        zip_path = create_test_zip(test_files)
        
        try:
            extracted_files = extract_zip_files(zip_path)
            
            # Check file is extracted in same directory as zip
            assert len(extracted_files) == 1
            assert os.path.exists(os.path.join(temp_dir, 'test.txt'))
        finally:
            os.unlink(zip_path)

def test_extract_zip_files_non_existent():
    """Test extraction from non-existent zip file."""
    with pytest.raises(FileNotFoundError):
        extract_zip_files('/path/to/non/existent/file.zip')

def test_extract_zip_files_nested():
    """Test extraction of nested files in zip."""
    test_files = {
        'dir1/file1.txt': 'nested content 1',
        'dir1/dir2/file2.txt': 'nested content 2'
    }
    
    with tempfile.TemporaryDirectory() as extract_dir:
        zip_path = create_test_zip(test_files)
        
        try:
            extracted_files = extract_zip_files(zip_path, extract_dir)
            
            # Check nested file paths
            assert len(extracted_files) == len(test_files)
            
            for filename, content in test_files.items():
                file_path = os.path.join(extract_dir, filename)
                assert os.path.exists(file_path)
                
                with open(file_path, 'r') as f:
                    assert f.read() == content
        finally:
            os.unlink(zip_path)

def test_extract_zip_files_multiple_files():
    """Test extracting multiple files with different types."""
    test_files = {
        'text.txt': 'text content',
        'image.png': b'\x89PNG\r\n\x1a\n',  # Simple PNG header
        'document.pdf': b'%PDF-1.7'  # Simple PDF header
    }
    
    with tempfile.TemporaryDirectory() as extract_dir:
        zip_path = create_test_zip(test_files)
        
        try:
            extracted_files = extract_zip_files(zip_path, extract_dir)
            
            assert len(extracted_files) == len(test_files)
            
            for filename, content in test_files.items():
                file_path = os.path.join(extract_dir, filename)
                assert os.path.exists(file_path)
                
                mode = 'rb' if isinstance(content, bytes) else 'r'
                with open(file_path, mode) as f:
                    assert f.read() == content
        finally:
            os.unlink(zip_path)