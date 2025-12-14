import os
from .config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.normpath(os.path.join(working_directory_abs, file_path))
        
        # Ensure the file path is within the working directory
        if not os.path.commonpath([working_directory_abs, file_path_abs]) == working_directory_abs:
            return f"    Error: Cannot read '{file_path}' as it is outside the permitted working directory"
        
        # Check if the file exists and is a file
        if not os.path.exists(file_path_abs) or not os.path.isfile(file_path_abs):
            return f'    Error: File not found or is not a regular file: "{file_path}"'
        
        with open(file_path_abs, 'r') as f:
            content = f.read(MAX_CHARS)
            if len(content) == MAX_CHARS:
                content += '[...File "{file_path}" truncated at 10000 characters]'
            return content
    except Exception as e:
        return f"    Error: {str(e)}"