#!/home/patricksutton/git/ai_agent/bin/python3

import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

from prompts import system_prompt
from call_function import call_function, available_functions

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

    generate_content(client, messages, verbose)

    # conversation = []
    # conversation.append(["User: " + user_prompt],
    #                     ["Model: " + function_responses.candidates],
    #                     ["Tool: " + function_responses.parts[0].function_response.response])

    iteration_to_solution(conversation=conversation)

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
            model='gemini-2.0-flash-001', 
            contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
        )
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if not response.function_calls:
        return response.text
    
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

# def iteration_to_solution (conversation)

if __name__ == "__main__":
    main()
