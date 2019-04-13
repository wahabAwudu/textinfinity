from rest_framework.serializers import ModelSerializer

from .models import Wallet, Deposit


class WalletModelSerializer(ModelSerializer):

    class Meta:
        model = Wallet
        fields = [
            'id',
            'user',
            'current_balance',
        ]
        read_only_fields = [
            'id',
            'current_balance',
            'user',
        ]


class DepositModelSerializer(ModelSerializer):

    class Meta:
        model = Deposit
        fields = [
            'id',
            'user',
            'ref_code',
            'status',
            'value',
            'created_at',
            'modified_at',
        ]
        read_only_fields = [
            'id',
            'ref_code',
            'created_at',
            'modified_at',
        ]
