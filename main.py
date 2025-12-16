import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file
from functions.call_function import call_function

def main():
    load_dotenv()
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not found in environment variables.")
    
    print("Initializing Gemini AI client...")
    
    client = genai.Client(api_key=api_key)
    
    # Set some hard-coded parameters
    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read File contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
    model = "gemini-2.5-flash"
    
    # Setup the aviable functions
    available_functions = types.Tool(
        function_declarations=[schema_get_files_info, schema_get_file_content, schema_write_file, schema_run_python_file],
    )
        
    # Get a prompt from the user
    parser = argparse.ArgumentParser(description="Cyberis AI Assistant")
    parser.add_argument('user_prompt', type=str, help='How can I assist you today?')
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    
    # Generate content using the Gemini model
    response = client.models.generate_content(
        model=model, 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    
    # If The User Wants Verbose output print that here
    if args.verbose:
        if not response.usage_metadata:
            raise RuntimeError("No usage metadata found in the response.")
        print(f'User prompt: {args.user_prompt}')
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    # Print the response and tool calls if any
    print(f"Response:\n{response.text}")
    results = []
    if response.function_calls:
        for call in response.function_calls:
            # Call the function and print the result
            function_response = call_function(call, verbose=args.verbose)
            try:
                if function_response.parts[0].response["result"]:
                    results.append(function_response.parts[0])
                else:
                    raise RuntimeError("No result found in function response.")
            except Exception as e:
                raise RuntimeError(f"Error processing function response: {str(e)}")
            print(f"Calling function: {call.name}({call.args})")
            if args.verbose:
                print(f"-> {function_response.parts[0].function_response.response}")
                
    if results:
        pass  #TODO: Handle multiple function call results if needed

if __name__ == "__main__":
    main()
