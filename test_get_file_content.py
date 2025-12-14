# Test out Get File Content function
import os
from functions.get_file_content import get_file_content

def test_get_file_content():
    # Test case 1: Valid file within working directory (truncated to avoid long output)
    results = get_file_content("calculator", "lorem-test.txt")
    print(f'Result for valid file "lorem-test.txt":\n{results}\n')

    # Test case 2: Valid file within working directory
    results = get_file_content("calculator", "main.py")
    print(f'Result for valid file "main.py":\n{results}\n')

    # Test case 3: Valid file in subdirectory
    results = get_file_content("calculator", "pkg/calculator.py")
    print(f'Result for valid file "pkg/calculator.py":\n{results}\n')

    # Test case 4: Invalid file (outside working directory)
    results = get_file_content("calculator", "/bin/cat")
    print(f'Result for invalid file "/bin/cat":\n{results}\n')

    # Test case 5: Non-existent file in a subdirectory
    results = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f'Result for non-existent file "pkg/does_not_exist.py":\n{results}\n')
    
if __name__ == "__main__":
    test_get_file_content()