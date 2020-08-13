import config
from flask import Flask, Response, request
from twilio import twiml
from twilio.rest import TwilioRestClient

app = Falsk(__name__)
client = TwilioRestClient(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)

@app.route('/incall', method=['POST'])
def inbound_call():
  response=twiml.Response()
  response.addSay("Thanks")
  return Response(str(response), 200, mimetype="application/xml")