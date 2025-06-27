import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

from prompts import system_prompt
from call_function import call_function, available_functions
from config import MAX_ITERS

def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith('--')]
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "<your prompt here>"')
        print('Example: python main.py "How do I build a calculator in Python?"')
        sys.exit(1)
    user_prompt = " ".join(args)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user",parts=[types.Part(text=user_prompt)]),
    ]

    for i in range(MAX_ITERS):
        candidates, function_responses = generate_content(client, messages, verbose)
        for candidate in candidates:
            messages.append(candidate.content)
        if function_responses == None:
            print(messages[-1].parts[0].text)
            break
        else:
            messages.append(types.Content(role='tool', parts=function_responses))
    

    # print(messages[-1])
    # generate_content(client, messages, verbose)

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
            model='gemini-2.0-flash-001', 
            contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
        )
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
        # print("Response: ", response.text)

    if not response.function_calls:
        return response.candidates, None
    
    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}") 
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting")
    return response.candidates, function_responses
    
    

if __name__ == "__main__":
    main()
