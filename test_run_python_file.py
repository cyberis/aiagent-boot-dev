import os
from functions.run_python_file import run_python_file

def test_run_python_file():
    # Test case 1: The Main Python file - should return usage info
    results = run_python_file("calculator", "main.py")
    print(f'Result for valid Python file "main.py":\n{results}\n')

    # Test case 2: The Main Python file with arguments - should return 8
    results = run_python_file("calculator", "main.py", ["3 + 5"])
    print(f'Result for valid Python file "main.py with arguments":\n{results}\n')

    # Test case 3: Run tests - should return test results
    results = run_python_file("calculator", "tests.py")
    print(f'Result for running tests "tests.py":\n{results}\n')

    # Test case 4: Run file in parent directory - should return error
    results = run_python_file("calculator", "../main.py", [])
    print(f'Result for Python file "../main.py":\n{results}\n')
    
    # Test case 5: Non-existent Python file - should return error
    results = run_python_file("calculator", "nonexistent.py")
    print(f'Result for non-existent Python file "nonexistent.py":\n{results}\n')

    # Test case 6: Non-Python file- should return error
    results = run_python_file("calculator", "lorem.txt")
    print(f'Result for non-Python file "lorem.txt":\n{results}\n')
    
if __name__ == "__main__":
    test_run_python_file()