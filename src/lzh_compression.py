import io
import struct

class LZHCompressor:
    """
    LZH (Lempel-Ziv-Huffman) Compression Implementation
    
    This is a basic implementation of LZH compression algorithm.
    Designed to handle byte-level preservation.
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
        
        # For small or non-compressible data, return as-is
        if len(data) < 32:
            return data
        
        output = bytearray()
        original_length = len(data)
        
        # Add original length as header
        output.extend(struct.pack('<I', original_length))
        
        current_pos = 0
        window_size = 4096
        look_ahead_size = 32
        
        while current_pos < len(data):
            # Find best match in sliding window
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
            if best_length > 4:
                # Compression token
                output.append(0xFF)  # Compression flag
                output.extend(struct.pack('<H', best_offset))  # Offset
                output.extend(struct.pack('<B', best_length))  # Length
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
        
        # If data looks uncompressed or is too small, return as-is
        if len(compressed_data) <= 4 or 0xFF not in compressed_data:
            return compressed_data
        
        # Extract original length
        try:
            original_length = struct.unpack('<I', compressed_data[:4])[0]
        except struct.error:
            return compressed_data
        
        output = bytearray()
        i = 4  # Start after length header
        
        while i < len(compressed_data):
            if compressed_data[i] == 0xFF:  # Compression flag
                if i + 3 >= len(compressed_data):
                    output.extend(compressed_data[i:])
                    break
                
                try:
                    offset = struct.unpack('<H', compressed_data[i+1:i+3])[0]
                    length = compressed_data[i + 3]
                except struct.error:
                    output.append(compressed_data[i])
                    i += 1
                    continue
                
                # Sanity checks
                if length <= 0 or offset <= 0 or offset > len(output):
                    output.append(compressed_data[i])
                    i += 1
                    continue
                
                # Reconstruct matched sequence
                start_pos = len(output) - offset
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
        
        # Ensure output matches original length if possible
        return bytes(output[:original_length])