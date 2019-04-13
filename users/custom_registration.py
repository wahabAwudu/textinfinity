from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from allauth.utils import get_username_max_length
from allauth.account import app_settings as allauth_settings
from rest_framework import serializers

from wallet.models import Wallet


class CustomRegistrationSerializer(RegisterSerializer):

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])

        # save new account
        user.save()

        # new wallet
        user_wallet = Wallet(user=user, current_balance=0.00)
        user_wallet.save()
        return user
