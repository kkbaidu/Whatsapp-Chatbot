from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from gem import reply_message

app = Flask(__name__)

@app.route("/whatsapp", methods=['GET', 'POST'])
def whatsapp_reply():
    message_body = request.form.get('Body', None)

    #bot reply
    ai_res = reply_message(message_body)

    response = MessagingResponse()

    response.message(ai_res)

    return str(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=5000)
