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
        
        # Sliding window and look-ahead buffer parameters
        window_size = 4096
        look_ahead_size = 16
        
        # Current position in input data
        current_pos = 0
        
        while current_pos < len(data):
            # Find longest match in sliding window
            best_length = 0
            best_offset = 0
            
            # Search backwards in the sliding window
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
                # Encode match as (offset, length)
                output.extend(struct.pack('<H', best_offset))
                output.extend(struct.pack('<B', best_length))
                current_pos += best_length
            else:
                # Literal byte
                output.extend(struct.pack('<B', data[current_pos]))
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
        input_stream = io.BytesIO(compressed_data)
        
        while input_stream.tell() < len(compressed_data):
            try:
                # Try to read match token
                offset_bytes = input_stream.read(2)
                length_byte = input_stream.read(1)
                
                if not offset_bytes or not length_byte:
                    # If we can't read full token, treat as literal
                    input_stream.seek(input_stream.tell() - 2)
                    literal_byte = input_stream.read(1)
                    output.extend(literal_byte)
                    continue
                
                offset = struct.unpack('<H', offset_bytes)[0]
                length = struct.unpack('B', length_byte)[0]
                
                # Retrieve previously written data
                start_pos = len(output) - offset
                
                # Handle case where offset is beyond current output
                if start_pos < 0:
                    # Treat as literal
                    input_stream.seek(input_stream.tell() - 3)
                    literal_byte = input_stream.read(1)
                    output.extend(literal_byte)
                    continue
                
                for i in range(length):
                    if start_pos + i < 0:
                        break
                    byte = output[start_pos + i]
                    output.append(byte)
            
            except (struct.error, IndexError):
                # If any error occurs, try to read as literal
                try:
                    input_stream.seek(input_stream.tell() - 2)
                    literal_byte = input_stream.read(1)
                    if not literal_byte:
                        break
                    output.extend(literal_byte)
                except Exception:
                    break
        
        return bytes(output)