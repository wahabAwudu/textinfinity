from django.template.loader import render_to_string

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from .models import Wallet, Deposit
from .serializers import WalletModelSerializer, DepositModelSerializer


class WalletModelViewset(ModelViewSet):
    model = Wallet
    serializer_class = WalletModelSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user.id)


class DepositModelViewset(ModelViewSet):
    model = Deposit
    serializer_class = DepositModelSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user.id)
