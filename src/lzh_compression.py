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
        output = io.BytesIO()
        
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
                output.write(struct.pack('&lt;HB', best_offset, best_length))
                current_pos += best_length
            else:
                # Literal byte
                output.write(struct.pack('B', data[current_pos]))
                current_pos += 1
        
        return output.getvalue()
    
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
        
        output = io.BytesIO()
        input_stream = io.BytesIO(compressed_data)
        
        while True:
            # Try to read token
            try:
                # Attempt to read match token
                offset_bytes = input_stream.read(2)
                length_byte = input_stream.read(1)
                
                if not offset_bytes or not length_byte:
                    break
                
                offset = struct.unpack('&lt;H', offset_bytes)[0]
                length = struct.unpack('B', length_byte)[0]
                
                # Retrieve previously written data
                current_output = output.getvalue()
                start_pos = len(current_output) - offset
                
                for i in range(length):
                    byte = current_output[start_pos + i]
                    output.write(struct.pack('B', byte))
            
            except (struct.error, IndexError):
                # If match token fails, try literal byte
                try:
                    literal_byte = input_stream.read(1)
                    if not literal_byte:
                        break
                    output.write(literal_byte)
                except Exception:
                    break
        
        return output.getvalue()