import twilio
from twilio.rest import TwilioRestClient

try:
	account_sid = "xxxxx"
	auth_token  = "xxxx"
	client = TwilioRestClient(account_sid, auth_token)
	 
	message = client.messages.create(
		body="Test message. Does this work?",
	    to="+0000",    
	    from_="+0000") 
	print message.sid

except twilio.TwilioRestException as e:
    print e