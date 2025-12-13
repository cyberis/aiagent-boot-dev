import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not found in environment variables.")
    
    print("Initializing Gemini AI client...")
    
    client = genai.Client(api_key=api_key)
    
    # Get a prompt from the user
    parser = argparse.ArgumentParser(description="Cyberis AI Assistant")
    parser.add_argument('user_prompt', type=str, help='How can I assist you today?')
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    
    # Generate content using the Gemini model
    response = client.models.generate_content(model="gemini-2.5-flash", contents=messages)
    
    # If The User Wants Verbose output print that here
    if args.verbose:
        if not response.usage_metadata:
            raise RuntimeError("No usage metadata found in the response.")
        print(f'User prompt: {args.user_prompt}')
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    # Print the response
    print(f"Response:\n{response.text}")
    

if __name__ == "__main__":
    main()
