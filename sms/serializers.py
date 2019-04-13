from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CurrentUserDefault

from .models import Message


class MessageModelSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(default=CurrentUserDefault(), read_only=True)

    class Meta:
        model = Message
        fields = [
            'id',
            'user',
            'list',
            'text',
            'status',
        ]
        read_only_fields = [
            'id',
        ]
