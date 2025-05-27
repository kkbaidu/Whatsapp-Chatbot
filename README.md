# WhatsApp AI Chatbot

This project implements a WhatsApp chatbot that uses a generative AI model (Google's Gemini Pro) to respond to incoming messages. It leverages Twilio for WhatsApp messaging integration and Flask to create a webhook for receiving messages.

## Project Structure

The project consists of the following main Python files:

*   **`gem.py`**: Handles the interaction with the Google Generative AI model. It takes a user's message, sends it to the Gemini Pro model, and returns the AI-generated response.
*   **`receive.py`**: Sets up a Flask web server to act as a webhook for Twilio. When a WhatsApp message is sent to the configured Twilio number, this script receives the message, uses `gem.py` to get an AI response, and sends the reply back via WhatsApp.
*   **`send.py`**: A utility script to send an initial message to a specified WhatsApp number using the Twilio API. This can be used for testing or initiating conversations.

## Prerequisites

Before you begin, ensure you have the following:

*   Python 3.7+
*   A Google API Key with the Generative Language API enabled.
*   A Twilio account with an active WhatsApp sandbox or a dedicated Twilio WhatsApp number.
*   `ngrok` or a similar tool to expose your local Flask server to the internet if running locally for Twilio webhook integration.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    Make sure your `requirements.txt` file is present and up to date, then run:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the root directory of the project and add the following variables with your actual credentials:

    ```env
    GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
    TWILIO_ACCOUNT_SID="YOUR_TWILIO_ACCOUNT_SID"
    TWILIO_AUTH_TOKEN="YOUR_TWILIO_AUTH_TOKEN"
    MY_PHONE_NUMBER="YOUR_WHATSAPP_PHONE_NUMBER_WITH_COUNTRY_CODE" # e.g., +1234567890
    ```
    *   `GOOGLE_API_KEY`: Your API key for Google Generative AI.
    *   `TWILIO_ACCOUNT_SID`: Your Twilio Account SID.
    *   `TWILIO_AUTH_TOKEN`: Your Twilio Auth Token.
    *   `MY_PHONE_NUMBER`: The WhatsApp-enabled phone number (including country code) you want to send test messages to (used by `send.py`) and potentially your test receiver number.

    **Note:** `gem.py` directly uses `os.getenv('GOOGLE_API_KEY')`. `send.py` uses `python-dotenv` to load variables from `.env`. `receive.py` doesn't directly handle environment variables for API keys, but `gem.py` (which it uses) does. For consistency and security, it's good practice to manage all sensitive keys via environment variables and ensure they are not hardcoded.

## Running the Chatbot

1.  **Expose your local server (if running locally):**
    If you are running the Flask server (`receive.py`) on your local machine, you need to expose it to the internet so Twilio can send webhook requests to it. Use a tool like `ngrok`.
    ```bash
    ngrok http 5000
    ```
    Note the `https` forwarding URL provided by `ngrok`.

2.  **Configure Twilio WhatsApp Sandbox:**
    *   Go to your Twilio console and navigate to the WhatsApp Sandbox settings.
    *   Set the "WHEN A MESSAGE COMES IN" webhook URL to the `ngrok` forwarding URL (or your deployed server's URL) followed by `/whatsapp`. For example: `https://your-ngrok-url.ngrok.io/whatsapp`. Ensure the method is set to `HTTP POST`.

3.  **Start the Flask server:**
    Open a new terminal, navigate to the project directory, activate the virtual environment, and run:
    ```bash
    python receive.py
    ```
    The server will start, typically on `http://0.0.0.0:5000/`.

4.  **Send a test message (optional):**
    You can use `send.py` to send an initial message to your WhatsApp number. First, ensure `MY_PHONE_NUMBER` in your `.env` file is set to your personal WhatsApp number (including the `whatsapp:` prefix and country code, e.g., `whatsapp:+1234567890`).
    ```bash
    python send.py
    ```

5.  **Test the chatbot:**
    Send a message from your WhatsApp number to the Twilio Sandbox number. The chatbot should reply via the AI model.

## How it Works

1.  A user sends a message to your Twilio WhatsApp number.
2.  Twilio forwards this message to the webhook URL you configured (your Flask app's `/whatsapp` endpoint handled by `receive.py`).
3.  The Flask app (`receive.py`) extracts the message body.
4.  It calls the `reply_message` function in `gem.py`.
5.  `gem.py` sends the message to the Google Generative AI API.
6.  The AI model generates a response.
7.  `receive.py` sends this response back to the user via Twilio.

---

This `README.md` provides a good overview, setup instructions, and operational details for the project.
