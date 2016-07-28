#! /usr/bin/env python3

from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "AC76f5be68b42f0bc0e6fe972b8cbe8f5e" 
AUTH_TOKEN = "f4b4c247e95893b0d6061687422c69aa" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

message = client.sms.messages.create(body="learning twilio with udacity",
                                     to="+61497861969",
                                     from_="+61419865493")

print(message.sid)
