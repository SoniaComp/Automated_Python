import config
from flask import Flask, Response, request
from twilio import twiml
from twilio.rest import TwilioRestClient

app = Falsk(__name__)
client = TwilioRestClient(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)

@app.route('/call', method=['POST'])
def outbound_call():
  response=twiml.Response()
  call=client.calls.create(
    to=config.MYNUMBER,
    from_=config.CALLERID,
    record='true',
    url=config.BASE_URL+'/answer_url'
  )
  return Response(str(response), 200, mimetype="application/xml")

@app.route('/answer_url', methods=['POST'])
def answer_url():
  response=twiml.Response()
  response.addSay("Hey!")
  return Response(str(response), 200, mimetype="application/xml")