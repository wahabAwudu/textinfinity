from decouple import Csv, config
from twilio.rest import Client
import requests


# send Mnotify sms
def mnotify_sms(sender, message, recipients):
    url = 'https://api.mnotify.com/api/sms/quick'
    params = {
        "key": config('MNOTIFY_API_V2_KEY'),
        "recipient[]": recipients,
        "message": message,
        "sender": sender,
    }
    # send the sms and return response
    resp = requests.post(url, data=params)
    return resp.json()
    # end mnotify sms


# send hubtel sms
def hubtel_sms(sender, message, recipients):
    url = "https://api.hubtel.com/v1/messages/send"
    resp = None
    for i in range(len(recipients)):
        params = {
            "From": sender,
            "To": recipients[i],
            "Content": message,
            "ClientId": config('HUBTEL_CLIENT_ID'),
            "ClientSecret": config('HUBTEL_CLIENT_SECRET'),
            "RegisteredDelivery": "true"
        }
        resp = requests.get(url, params=params)

    return resp
    # end hubtel sms


# send sms using twilio
def twilio_sms(recipient, message):
    twilio_account_sid = config('TWILIO_ACCOUNT_SID')
    twilio_auth_token = config('TWILIO_AUTH_TOKEN')
    twilio_number = config('TWILIO_NUMBER')

    client = Client(twilio_account_sid, twilio_auth_token)

    sms = client.messages.create(
        to=recipient, from_=twilio_number, body=message,
        # status_callback="http://omakunta.com/"
                                    )
    return sms
    # end twilio sms
