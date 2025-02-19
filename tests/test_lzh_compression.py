import pytest
from src.lzh_compression import LZHCompressor

def test_compress_decompress_simple_text():
    """Test compression and decompression of simple text"""
    original_data = b"Hello, world! This is a test of LZH compression."
    compressed = LZHCompressor.compress(original_data)
    decompressed = LZHCompressor.decompress(compressed)
    
    assert decompressed == original_data, "Decompression should match original data"
    assert len(compressed) < len(original_data), "Compressed data should be smaller"

def test_compress_decompress_repeated_data():
    """Test compression of data with repeated sequences"""
    original_data = b"abcabcabcabcabcabcabc" * 10
    compressed = LZHCompressor.compress(original_data)
    decompressed = LZHCompressor.decompress(compressed)
    
    assert decompressed == original_data, "Repeated data compression failed"
    assert len(compressed) < len(original_data), "Repeated data should compress well"

def test_compress_decompress_binary_data():
    """Test compression of binary data"""
    original_data = bytes(range(256)) * 5
    compressed = LZHCompressor.compress(original_data)
    decompressed = LZHCompressor.decompress(compressed)
    
    assert decompressed == original_data, "Binary data compression failed"

def test_invalid_input_types():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        LZHCompressor.compress("string input")
    
    with pytest.raises(TypeError):
        LZHCompressor.decompress("string input")

def test_empty_input():
    """Test compression and decompression of empty input"""
    empty_data = b""
    compressed = LZHCompressor.compress(empty_data)
    decompressed = LZHCompressor.decompress(compressed)
    
    assert decompressed == empty_data, "Empty input compression failed"
    assert len(compressed) == 0, "Compressed empty input should be empty"