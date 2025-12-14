import os
from functions.write_file import write_file

def test_write_file():
    # Test case 1: Valid write within working directory
    results = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(f'Result for writing to valid file "lorem.txt":\n{results}\n')

    # Test case 2: Valid write in subdirectory
    results = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f'Result for writing to valid file "pkg/morelorem.txt":\n{results}\n')

    # Test case 3: Invalid write (outside working directory)
    results = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f'Result for writing to invalid file "/tmp/temp.txt":\n{results}\n')

    # Test case 4: Write to a file where the path is a directory
    os.makedirs("calculator/pkg/test_dir", exist_ok=True)
    results = write_file("calculator", "pkg/test_dir", "this should fail")
    print(f'Result for writing to a directory "pkg/test_dir":\n{results}\n')
    os.rmdir("calculator/pkg/test_dir")  # Clean up
    
if __name__ == "__main__":
    test_write_file()