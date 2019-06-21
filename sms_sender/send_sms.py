import os

from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

ph = input("ENTER PHONE NUMBER TO SEND THE MESSAGE: ")
message = input("ENTER TEXT YOU WANT TO SEND: ")

client.messages.create(
    to=ph,
    from_="+12015145735",
    body=message
)
