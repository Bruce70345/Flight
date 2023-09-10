from twilio.rest import Client

TWILIO_SID = "AC8a74c24e6be08ef0575f0e3d5f914429"
TWILIO_AUTH_TOKEN = "74b9ca57c61d7342d2b826210587233a"
TWILIO_VIRTUAL_NUMBER = "+15856785110"
TWILIO_VERIFIED_NUMBER = "+886976912590"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        #print(message.sid)