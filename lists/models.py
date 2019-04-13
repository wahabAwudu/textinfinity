from django.db import models
from django.conf import settings

from users.choices import active


class List(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    status = models.CharField(max_length=20, default=active)

    def __str__(self):
        return str(self.name)


class Number(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return str(self.phone)
