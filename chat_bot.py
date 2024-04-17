from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=['GET', 'POST'])
def whatsapp_reply():
    response = MessagingResponse()

    response.message("Thank you for contacting KingsAccess")

    return str(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=8080)
