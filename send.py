"""
Utility script to send a WhatsApp message using the Twilio API.

This script loads Twilio credentials and a target phone number from environment
variables (or a .env file) and sends a predefined message to the specified
WhatsApp number. It's useful for testing the Twilio setup or initiating
a conversation.
"""
import os
from dotenv import load_dotenv
from twilio.rest import Client

# Load environment variables from a .env file
load_dotenv()

# Retrieve Twilio Account SID and Auth Token from environment variables
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

# Initialize the Twilio client
client = Client(account_sid, auth_token)

# Define the sender's WhatsApp number (Twilio Sandbox or your Twilio number)
from_whatsapp_number = 'whatsapp:+14155238886' # Default Twilio sandbox number
# Define the recipient's WhatsApp number from an environment variable
to_whatsapp_number = 'whatsapp:' + os.environ['MY_PHONE_NUMBER']

# Create and send the message
client.messages.create(
    body='Welcome Kingsley, how may I do for you😊?',  # The message content
    from_=from_whatsapp_number,                         # Sender's WhatsApp number
    to=to_whatsapp_number                               # Recipient's WhatsApp number
)
