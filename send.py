import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:' + os.environ['MY_PHONE_NUMBER']

client.messages.create(body='Welcome Kingsley, how may I do for you😊?', from_=from_whatsapp_number, to=to_whatsapp_number)