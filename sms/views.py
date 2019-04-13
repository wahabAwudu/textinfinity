from decouple import config, Csv
import requests

from django.template.loader import render_to_string

from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import list_route

from twilio.rest import Client

from .models import Message
from .serializers import MessageModelSerializer

from users.choices import processing, active, confirmed
from lists.models import Number


class MessageModelViewset(ModelViewSet):
    model = Message
    serializer_class = MessageModelSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user.id)

    # send hubtel sms
    def hubtel_sms(self, sender, message, recipients):
        url = "https://api.hubtel.com/v1/messages/send"

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

        response = None
        if resp.status_code == 201:
            response = Response({"detail": "Message Sent Successfully"})
        elif resp.status_code >= 400:
            response = Response({"detail": "Error Sending Message, Try Again"})
        return response
        # end hubtel sms

    # send sms using twilio
    def send_messages(self, recipient, message):
        twilio_account_sid = config('TWILIO_ACCOUNT_SID')
        twilio_auth_token = config('TWILIO_AUTH_TOKEN')
        twilio_number = config('TWILIO_NUMBER')

        client = Client(twilio_account_sid, twilio_auth_token)

        client.messages.create(to=recipient,
                               from_=twilio_number,
                               body=message,
                               # status_callback="http://omakunta.com/"
                               )

        return Response({"detail": "Message Sent"}, status=status.HTTP_200_OK)
        # end twilio sms

        # send Mnotify sms
    def mnotify_sms(self, sender, message, recipients):
        url = 'https://api.mnotify.com/api/sms/quick'
        params = {
            "key": config('MNOTIFY_API_V2_KEY'),
            "recipient[]": recipients,
            "message": message,
            "sender": sender,
        }
        # send the request
        resp = requests.post(url, data=params)
        return resp.json()
        # end mnotify sms

        # create the message for logs reason
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        # get contacts using list as reference
        list = request.data['list']
        contacts = Number.objects.filter(list=list)

        # sms method arguments
        sender = request.data['sender']
        message = request.data['text']
        recipients = contacts

        # return response from sms method
        sms_response = self.mnotify_sms(sender, message, recipients)

        # save message after successful sending
        serializer.is_valid(raise_exception=True)
        serializer.save(status=confirmed, user=request.user)

        return Response(
            sms_response,
            status=status.HTTP_201_CREATED,
            headers=self.get_success_headers(serializer.data)
        )
