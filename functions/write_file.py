import os
from google.genai import types

# Define the useage of this function as an LLM tool
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to write file contents to, relative to the working directory. If not provided, the file is in the working directory itself.",
            ),
        },
    ),
)

def write_file(working_directory, file_path, content):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.normpath(os.path.join(working_directory_abs, file_path))
        
        # Ensure the file path is within the working directory
        if not os.path.commonpath([working_directory_abs, file_path_abs]) == working_directory_abs:
            return f"    Error: Cannot write to '{file_path}' as it is outside the permitted working directory"
        
        # Check if the file_path is a file
        if os.path.exists(file_path_abs) and not os.path.isfile(file_path_abs):
            return f'    Error: File not found or is not a regular file: "{file_path}"'
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path_abs), exist_ok=True)
        
        with open(file_path_abs, 'w') as f:
            f.write(content)
        return f"    Successfully wrote to '{file_path}' ({len(content)} characters written)"
    except Exception as e:
        return f"    Error: {str(e)}"