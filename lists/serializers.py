from rest_framework.serializers import ModelSerializer

from .models import List, Number


class ListModelSerializer(ModelSerializer):

    class Meta:
        model = List
        fields = [
            'id',
            'user',
            'name',
        ]

        read_only_fields = [
            'id',
        ]


class NumberModelSerializer(ModelSerializer):

    class Meta:
        model = Number
        fields = [
            'id',
            'list',
            'digits',
        ]
        read_only_fields = [
            'id',
        ]
