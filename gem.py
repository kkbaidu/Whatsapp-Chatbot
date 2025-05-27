"""
Handles communication with the Google Generative AI API (Gemini Pro).

This script retrieves the Google API key from environment variables,
configures the generative AI model, and provides a function to get
AI-generated responses for given messages.
"""
import google.generativeai as genai
import os

# Retrieve the Google API key from environment variables
api_key = os.getenv('GOOGLE_API_KEY') #Paste API key here

# Ensure the API key is available
if not api_key:
    print("Error: Please set the GOOGLE_API_KEY environment variable.")
    exit(1)

# Configure the Google Generative AI client with the API key
genai.configure(api_key=api_key)

# Initialize the Generative Model (e.g., 'gemini-pro')
model = genai.GenerativeModel('gemini-pro')

def reply_message(client_message):
    """
    Generates an AI response to a given client message.

    Args:
        client_message (str): The message from the client (user).

    Returns:
        str: The AI-generated text response. Returns an error message
             if the generation fails.
    """
    try:
        # Generate content using the model
        response = model.generate_content(client_message)
        return response.text
    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred during message generation."
