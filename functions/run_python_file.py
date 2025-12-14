import os
import subprocess
from .config import MAX_TIME_SECONDS

def run_python_file(working_directory, file_path, args=[]):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.normpath(os.path.join(working_directory_abs, file_path))
        
        # Ensure the file path is within the working directory
        if not os.path.commonpath([working_directory_abs, file_path_abs]) == working_directory_abs:
            return f'    Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        # Check if the file exists and is a file
        if not os.path.exists(file_path_abs) or not os.path.isfile(file_path_abs):
            return f'    Error: File "{file_path}" not found.'
        
        # Check if this is a python file
        if not file_path_abs.endswith('.py'):
            return f'    Error: "{file_path}" is not a Python file.'
        
        # Prepare the command
        command = ['python', file_path] + args
        
        # Run the command with a timeout
        result = subprocess.run(command, capture_output=True, text=True, timeout=MAX_TIME_SECONDS, cwd=working_directory_abs)
        
        # Collect the results of the run and return these
        output = f'STDOUT: {result.stdout}\nSTDERR: {result.stderr}\n'
        
        # If there was no output, indicate that
        if not result.stdout and not result.stderr:  
            output += 'No output produced\n'
        
        # Check for errors
        if result.returncode != 0:
            output += f"    Error: Process exited with code {result.returncode}"
        
        # Tell the caller how it went
        return output
    
    except subprocess.TimeoutExpired:
        return f"    Error: Execution of '{file_path}' timed out after {MAX_TIME_SECONDS} seconds"
    except Exception as e:
        return f"    Error: executing Python file: {str(e)}"
