from django.template.loader import render_to_string

from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import list_route

from .models import Message
from .serializers import MessageModelSerializer

from users.choices import processing, active, confirmed
from lists.models import Number

from .sms_triggers import mnotify_sms, twilio_sms, hubtel_sms


class MessageModelViewset(ModelViewSet):
    model = Message
    serializer_class = MessageModelSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user.id)

    @list_route(methods=['POST'])
    def send_sms(self, request):
        sender_id = request.data['sender_id']
        message = request.data['message']
        recipients = request.data['recipients']
        serializer = self.get_serializer(data=request.data)
        # send sms with mnotify
        status_code = None
        response = mnotify_sms(sender_id, message, recipients)

        if response['code'] == '2000':
            status_code = status.HTTP_200_OK
        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        print(response)
        return Response({'detail': 'messages sent', }, status=status_code)

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

        # send sms and return response
        sms_response = mnotify_sms(sender, message, recipients)

        # save message after successful sending
        serializer.is_valid(raise_exception=True)
        serializer.save(status=confirmed, user=request.user)

        return Response(
            sms_response,
            status=status.HTTP_201_CREATED,
            headers=self.get_success_headers(serializer.data)
        )
