from rest_framework.serializers import (
    ModelSerializer, 
    SerializerMethodField, 
    PrimaryKeyRelatedField,
)
from rest_framework import serializers

from .models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'phone',
        ]
        read_only_fields = [
            'id',
        ]


class VerifyEmailSerializer(serializers.Serializer):
    key = serializers.CharField()
