"""
Sets up a Flask web server to receive incoming WhatsApp messages via Twilio.

This script defines a webhook endpoint `/whatsapp` that Twilio calls when a message
is sent to the configured WhatsApp number. It extracts the message, gets an
AI-generated response using the `gem.py` module, and sends the reply back
to the user via Twilio's MessagingResponse.
"""
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from gem import reply_message

app = Flask(__name__)

@app.route("/whatsapp", methods=['GET', 'POST'])
def whatsapp_reply():
    """
    Handles incoming WhatsApp messages and sends an AI-generated reply.

    This function is triggered by Twilio when a message is received.
    It extracts the body of the incoming message, gets a response from
    the AI model via `reply_message`, and sends this response back to
    the sender.
    """
    # Extract the message body from the incoming Twilio request
    message_body = request.form.get('Body', None)

    # Get an AI-generated response using the reply_message function from gem.py
    ai_res = reply_message(message_body)

    # Create a Twilio MessagingResponse object to build the reply
    response = MessagingResponse()

    # Add the AI's response to the message object
    response.message(ai_res)

    # Return the response as a string to Twilio
    return str(response)

if __name__ == "__main__":
    # Run the Flask app on host 0.0.0.0 to be accessible externally
    # and set debug to False for production.
    app.run(host='0.0.0.0', debug=False, port=5000)
