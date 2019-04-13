# drf imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAdminUser
)
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from allauth.account.views import ConfirmEmailView

# django imports
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# apps imports
from .serializers import (
    UserModelSerializer,
    VerifyEmailSerializer,
)

from .models import User


class UserModelViewset(ModelViewSet):
    model = User
    permission_classes = [IsAuthenticated]
    serializer_class = UserModelSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


@api_view
def null_view(request):
    return Response(status=status.HTTP_400_BAD_REQUEST)


class VerifyEmailView(APIView, ConfirmEmailView):
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def get_serializer(self, *args, **kwargs):
        return VerifyEmailSerializer(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.kwargs['key'] = serializer.validated_data['key']
        confirmation = self.get_object()
        confirmation.confirm(self.request)
        return Response({'detail': _('ok')}, status=status.HTTP_200_OK)
