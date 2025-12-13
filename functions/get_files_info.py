import os

def get_files_info(working_directory, directory="."):
    try:
        # Get absolute paths
        working_directory_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_directory_abs, directory))
        
        # Ensure the target directory is within the working directory
        valiid_target_dir = os.path.commonpath([working_directory_abs, target_dir]) == working_directory_abs
        
        # if not return an error string
        if not valiid_target_dir:
            return f'    Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        # List files in the target directory
        files = os.listdir(target_dir)
        files_info = []
        for file_name in files:
            file_path = os.path.join(target_dir, file_name)
            is_directory = str(os.path.isdir(file_path))
            file_size = os.path.getsize(file_path)
            files_info.append({
                "file_name": file_name,
                "is_dir": is_directory,
                "file_size": file_size
            })
        
        # Return a formatted string of files info
        files_info_str = "\n".join([f"  - {info['file_name']}: file_size={info['file_size']} bytes, is_dir={info['is_dir']}" for info in files_info])
        return files_info_str
    
    except Exception as e:
        return f"    Error: {str(e)}"