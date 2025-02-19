import io
import struct

class LZHCompressor:
    """
    LZH (Lempel-Ziv-Huffman) Compression Implementation
    
    This is a basic implementation of LZH compression algorithm.
    """
    
    @staticmethod
    def compress(data):
        """
        Compress input data using LZH compression algorithm.
        
        Args:
            data (bytes): Input data to compress
        
        Returns:
            bytes: Compressed data
        """
        if not isinstance(data, bytes):
            raise TypeError("Input must be bytes")
        
        # If data is too small, return as-is
        if len(data) < 32:
            return data
        
        # Create output buffer
        output = bytearray()
        
        # Sliding window parameters
        window_size = 4096
        look_ahead_size = 32
        
        current_pos = 0
        
        while current_pos < len(data):
            # Find the best match in the sliding window
            best_length = 0
            best_offset = 0
            
            search_start = max(0, current_pos - window_size)
            search_end = current_pos
            
            for offset in range(search_start, search_end):
                match_length = 0
                max_match = min(look_ahead_size, len(data) - current_pos)
                
                while (match_length < max_match and 
                       data[offset + match_length] == data[current_pos + match_length]):
                    match_length += 1
                
                # More aggressive matching
                if match_length > best_length:
                    best_length = match_length
                    best_offset = current_pos - offset
            
            # Write compression token
            if best_length > 4:
                # Mark as compressed token
                output.append(0xFF)  # Compression flag
                output.extend(struct.pack('<H', best_offset))  # Use 2-byte unsigned short
                output.extend(struct.pack('<B', best_length))
                current_pos += best_length
            else:
                # Literal byte
                output.append(data[current_pos])
                current_pos += 1
        
        return bytes(output)
    
    @staticmethod
    def decompress(compressed_data):
        """
        Decompress LZH compressed data.
        
        Args:
            compressed_data (bytes): Compressed input data
        
        Returns:
            bytes: Decompressed data
        """
        if not isinstance(compressed_data, bytes):
            raise TypeError("Input must be bytes")
        
        # If data doesn't look compressed or is too small, return as-is
        if len(compressed_data) <= 4 or 0xFF not in compressed_data:
            return compressed_data
        
        output = bytearray()
        i = 0
        
        while i < len(compressed_data):
            if compressed_data[i] == 0xFF:  # Compression flag
                if i + 3 >= len(compressed_data):
                    # If truncated, add remaining bytes as literal
                    output.extend(compressed_data[i:])
                    break
                
                # Extract offset and length
                try:
                    offset = struct.unpack('<H', compressed_data[i+1:i+3])[0]
                    length = compressed_data[i + 3]
                except struct.error:
                    # If struct unpacking fails, treat as literal
                    output.append(compressed_data[i])
                    i += 1
                    continue
                
                # Sanity check for offset and length
                if length <= 0 or offset <= 0 or offset > len(output):
                    output.append(compressed_data[i])
                    i += 1
                    continue
                
                # Retrieve previous data
                start_pos = len(output) - offset
                
                # Reconstruct the matched sequence with safety checks
                for j in range(length):
                    if start_pos + j < 0 or start_pos + j >= len(output):
                        break
                    try:
                        output.append(output[start_pos + j])
                    except IndexError:
                        break
                
                i += 4
            else:
                # Literal byte
                output.append(compressed_data[i])
                i += 1
        
        return bytes(output)