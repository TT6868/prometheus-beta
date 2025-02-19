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
        
        # Create output buffer
        output = bytearray()
        
        # Sliding window parameters
        window_size = 256
        look_ahead_size = 8
        
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
                
                if match_length > best_length:
                    best_length = match_length
                    best_offset = current_pos - offset
            
            # Write compression token
            if best_length > 2:
                # Mark as compressed token
                output.append(0xFF)  # Compression flag
                output.extend(struct.pack('<B', best_offset))
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
        
        output = bytearray()
        i = 0
        
        while i < len(compressed_data):
            if compressed_data[i] == 0xFF:  # Compression flag
                if i + 2 >= len(compressed_data):
                    break
                
                # Extract offset and length
                offset = compressed_data[i + 1]
                length = compressed_data[i + 2]
                
                # Retrieve previous data
                start_pos = len(output) - offset
                
                # Reconstruct the matched sequence
                for j in range(length):
                    if start_pos + j < 0:
                        break
                    output.append(output[start_pos + j])
                
                i += 3
            else:
                # Literal byte
                output.append(compressed_data[i])
                i += 1
        
        return bytes(output)