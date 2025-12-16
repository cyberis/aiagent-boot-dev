from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def call_function(function_call_part, verbose=False):
    """Calls a function based on the provided function call part.

    Args:
        function_call_part: The function call part containing the function name and arguments.
        verbose: If True, prints verbose output.

    Returns:
        The result of the function call.
    """
    function_name = function_call_part.name
    arguments = function_call_part.args
    arguments["working_directory"] = "./calculator"  # Inject the working directory

    if verbose:
        print(f"Calling function: {function_name}({arguments})")
    else:
        print(f" - Calling function: {function_name}")

    # Call the appropriate function
    vtable = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "write_file": write_file,
        "run_python_file": run_python_file,
    }

    if function_name in vtable:
        function_result = vtable[function_name](**arguments)
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
        
    # Return the function result as a tool response
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )    