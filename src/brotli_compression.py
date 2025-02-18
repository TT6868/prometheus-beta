import brotli

def compress_brotli(data, quality=11, mode=brotli.MODE_GENERIC):
    """
    Compress data using Brotli compression algorithm.
    
    Args:
        data (bytes or str): The data to be compressed. If str, it will be encoded to bytes.
        quality (int, optional): Compression level. Defaults to 11 (maximum compression).
                                 Range is 0-11, where 0 is fastest, 11 is most compressed.
        mode (int, optional): Compression mode. Defaults to MODE_GENERIC.
                              Can be MODE_GENERIC, MODE_TEXT, or MODE_FONT.
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes or str
        ValueError: If quality is not between 0 and 11
    """
    # Validate input type
    if not isinstance(data, (bytes, str)):
        raise TypeError("Input must be bytes or str")
    
    # Convert str to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate compression quality
    if not 0 <= quality <= 11:
        raise ValueError("Compression quality must be between 0 and 11")
    
    # Validate compression mode
    valid_modes = [brotli.MODE_GENERIC, brotli.MODE_TEXT, brotli.MODE_FONT]
    if mode not in valid_modes:
        raise ValueError(f"Invalid compression mode. Must be one of {valid_modes}")
    
    # Compress the data
    compressed_data = brotli.compress(data, mode=mode, quality=quality)
    
    return compressed_data

def decompress_brotli(compressed_data):
    """
    Decompress Brotli compressed data.
    
    Args:
        compressed_data (bytes): Brotli compressed data
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        brotli.error: If decompression fails
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Decompress the data
    decompressed_data = brotli.decompress(compressed_data)
    
    return decompressed_data