import os
import zipfile

def extract_zip_files(zip_path, extract_path=None):
    """
    Extract all files from a given zip archive.
    
    Args:
        zip_path (str): Path to the zip file to extract.
        extract_path (str, optional): Destination directory for extraction. 
                                      If None, extracts to the zip file's directory.
    
    Returns:
        list: List of paths to extracted files.
    
    Raises:
        FileNotFoundError: If the zip file does not exist.
        zipfile.BadZipFile: If the zip file is corrupted or invalid.
        PermissionError: If there are insufficient permissions to extract files.
    """
    # Validate zip file exists
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"Zip file not found: {zip_path}")
    
    # Determine extraction path
    if extract_path is None:
        extract_path = os.path.dirname(zip_path)
    
    # Ensure extraction directory exists
    os.makedirs(extract_path, exist_ok=True)
    
    # List to store extracted file paths
    extracted_files = []
    
    # Open and extract zip file
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Extract all files
            for file in zip_ref.namelist():
                # Construct full file path
                extracted_file_path = os.path.normpath(os.path.join(extract_path, file))
                
                # Prevent zip slip vulnerability by ensuring file is within extraction path
                if not extracted_file_path.startswith(os.path.abspath(extract_path)):
                    raise ValueError(f"Unsafe file path detected: {file}")
                
                # Extract file
                zip_ref.extract(file, extract_path)
                extracted_files.append(extracted_file_path)
    
    except zipfile.BadZipFile:
        raise zipfile.BadZipFile(f"Invalid or corrupted zip file: {zip_path}")
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to extract files to {extract_path}")
    
    return extracted_files