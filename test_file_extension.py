import os
import pytest
from file_extension import get_file_extension

def test_get_file_extension_normal_case():
    """Test getting extension for a typical file path"""
    assert get_file_extension('document.txt') == 'txt'
    assert get_file_extension('/path/to/document.pdf') == 'pdf'

def test_get_file_extension_multiple_dots():
    """Test files with multiple dots"""
    assert get_file_extension('archive.tar.gz') == 'gz'
    assert get_file_extension('/path/to/script.backup.py') == 'py'

def test_get_file_extension_no_extension():
    """Test files without an extension"""
    assert get_file_extension('README') == ''
    assert get_file_extension('/path/to/executable') == ''

def test_get_file_extension_dot_file():
    """Test dot files"""
    assert get_file_extension('.gitignore') == ''
    assert get_file_extension('/path/to/.env') == ''

def test_get_file_extension_edge_cases():
    """Test various edge cases"""
    assert get_file_extension('  file.txt  ') == 'txt'
    assert get_file_extension('file.TXT') == 'TXT'  # case-sensitive
    assert get_file_extension('file.') == ''