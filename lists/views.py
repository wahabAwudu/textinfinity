from django.template.loader import render_to_string

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import list_route

from .models import List, Number
from .serializers import ListModelSerializer, NumberModelSerializer


class ListModelViewset(ModelViewSet):
    model = List
    serializer_class = ListModelSerializer
    permission_classes = [IsAuthenticated, ]
    
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user.id)

    @list_route(methods=['POST', ], permission_classes=[IsAuthenticated, ])
    def save_contact_list(self, request):
        list_name = request.data['list_name']
        numbers = self.get_numbers
        print(numbers, ' ', list_name)

        # create list
        # new_list = List.objects.create(user=request.user, name=list_name)
        # new_list.save()

        # create phones

        return Response({"detail": "Done"})

    @property
    def get_numbers(self):
        numbers = ''
        return numbers


class NumberAdminModelViewset(ModelViewSet):
    model = Number
    serializer_class = NumberModelSerializer
    permission_classes = [IsAdminUser,]
    queryset = Number.objects.all()
