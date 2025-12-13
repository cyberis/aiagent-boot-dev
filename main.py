import os
from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not found in environment variables.")
    
    print("Initializing Gemini AI client...")
    
    client = genai.Client(api_key=api_key)
    
    # Example usage of the client
    content = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    print(f'User prompt: {content}')
    response = client.models.generate_content(model="gemini-2.5-flash", contents=content)
    
    # Print token usage
    if not response.usage_metadata:
        raise RuntimeError("No usage metadata found in the response.")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    # Print the response
    print(f"Response:\n{response.text}")
    

if __name__ == "__main__":
    main()
