from django.db import models
from django.conf import settings

from lists.models import List
from users.choices import processing


class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    draft = models.BooleanField(default=False)
    status = models.CharField(max_length=20, default=processing)

    def __str__(self):
        return str(self.text)
