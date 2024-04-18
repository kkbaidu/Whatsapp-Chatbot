import google.generativeai as genai 
import os

api_key = os.getenv('GOOGLE_API_KEY')

if not api_key:
    print("Error: Please set the GOOGLE_API_KEY environment variable.")
    exit(1)

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-pro')

def reply_message(client_message):
    try:
        response = model.generate_content(client_message)
        return response.text
    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred during message generation."
