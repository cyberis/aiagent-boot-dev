# Test Our get_files_info function
import os
from functions.get_files_info import get_files_info

def test_get_files_info():
    
    # Test case 1: Valid working directory
    results = get_files_info("calculator", ".")
    print(f'Result for current directory:\n{results}')
    
    # Test case 2: Valid subdirectory
    results = get_files_info("calculator", "pkg")
    print(f"\nResult for 'pkg' directory:\n{results}")
    
    # Test case 3: Invalid directory (outside working directory)
    results = get_files_info("calculator", "/bin")
    print(f"\nResult for '/bin' directory:\n{results}")
    
    # Test case 4: Parent directory (should be invalid)
    results = get_files_info("calculator", "../")
    print(f"\nResult for '../' directory:\n{results}")

if __name__ == "__main__":
    test_get_files_info()