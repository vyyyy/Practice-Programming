#! /usr/bin/env python3

from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = X 
AUTH_TOKEN = X 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

message = client.sms.messages.create(body="learning twilio with udacity",
                                     to="+61400000000",
                                     from_="+61400000000")

print(message.sid)
