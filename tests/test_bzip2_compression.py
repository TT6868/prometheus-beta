import pytest
import bz2
from src.bzip2_compression import compress_bzip2, decompress_bzip2

def test_compress_string():
    """Test compressing a string"""
    test_string = "Hello, world! This is a test of Bzip2 compression."
    compressed = compress_bzip2(test_string)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0
    assert compressed != test_string.encode('utf-8')

def test_compress_bytes():
    """Test compressing bytes"""
    test_bytes = b"Binary data for compression test"
    compressed = compress_bzip2(test_bytes)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0
    assert compressed != test_bytes

def test_decompress():
    """Test full compression and decompression cycle"""
    test_string = "Hello, world! This is a test of Bzip2 compression."
    compressed = compress_bzip2(test_string)
    decompressed = decompress_bzip2(compressed)
    assert decompressed.decode('utf-8') == test_string

def test_compression_levels():
    """Test different compression levels"""
    test_data = "Compression level test" * 100  # Longer data to show level differences
    
    # Test multiple compression levels
    for level in range(1, 10):
        compressed = compress_bzip2(test_data, compression_level=level)
        assert isinstance(compressed, bytes)
        assert len(compressed) > 0

def test_invalid_compression_level():
    """Test handling of invalid compression levels"""
    with pytest.raises(ValueError):
        compress_bzip2("Test", compression_level=0)
    with pytest.raises(ValueError):
        compress_bzip2("Test", compression_level=10)

def test_invalid_input_type():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        compress_bzip2(123)
    with pytest.raises(TypeError):
        decompress_bzip2("Not bytes")

def test_edge_cases():
    """Test edge cases"""
    # Empty string
    empty_compressed = compress_bzip2("")
    assert decompress_bzip2(empty_compressed) == b""

    # Unicode string
    unicode_string = "こんにちは世界"
    unicode_compressed = compress_bzip2(unicode_string)
    assert decompress_bzip2(unicode_compressed).decode('utf-8') == unicode_string

def test_large_data():
    """Test compression of large data"""
    large_data = "Large data test " * 10000
    compressed = compress_bzip2(large_data)
    decompressed = decompress_bzip2(compressed)
    assert decompressed.decode('utf-8') == large_data