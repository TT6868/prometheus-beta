import pytest
import brotli
from src.brotli_compression import compress_brotli, decompress_brotli

def test_compress_decompress_bytes():
    """Test compression and decompression of bytes"""
    original_data = b'Hello, this is a test of Brotli compression!'
    compressed = compress_brotli(original_data)
    assert compressed != original_data
    assert len(compressed) < len(original_data)
    
    decompressed = decompress_brotli(compressed)
    assert decompressed == original_data

def test_compress_decompress_str():
    """Test compression and decompression of string"""
    original_data = 'Hello, this is a test of Brotli compression!'
    compressed = compress_brotli(original_data)
    assert compressed != original_data.encode('utf-8')
    
    decompressed = decompress_brotli(compressed)
    assert decompressed == original_data.encode('utf-8')

def test_compression_qualities():
    """Test different compression qualities"""
    data = b'Test data for compression quality checks'
    
    # Test minimum and maximum quality levels
    compressed_min = compress_brotli(data, quality=0)
    compressed_max = compress_brotli(data, quality=11)
    
    assert len(compressed_min) >= len(compressed_max)

def test_compression_modes():
    """Test different compression modes"""
    data = b'Test data for compression mode checks'
    
    compressed_generic = compress_brotli(data, mode=brotli.MODE_GENERIC)
    compressed_text = compress_brotli(data, mode=brotli.MODE_TEXT)
    compressed_font = compress_brotli(data, mode=brotli.MODE_FONT)
    
    # Ensure different modes produce different compression
    assert len(set([len(compressed_generic), len(compressed_text), len(compressed_font)])) > 1

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        compress_brotli(123)
    
    with pytest.raises(TypeError):
        decompress_brotli('not bytes')

def test_invalid_compression_quality():
    """Test error handling for invalid compression quality"""
    with pytest.raises(ValueError):
        compress_brotli(b'test', quality=12)
    
    with pytest.raises(ValueError):
        compress_brotli(b'test', quality=-1)

def test_invalid_compression_mode():
    """Test error handling for invalid compression mode"""
    with pytest.raises(ValueError):
        compress_brotli(b'test', mode=999)

def test_decompression_error():
    """Test error handling for invalid compressed data"""
    with pytest.raises(brotli.error):
        decompress_brotli(b'invalid compressed data')

def test_large_data_compression():
    """Test compression of large data"""
    large_data = b'A' * 100000  # 100 KB of data
    compressed = compress_brotli(large_data)
    assert len(compressed) < len(large_data)
    
    decompressed = decompress_brotli(compressed)
    assert decompressed == large_data