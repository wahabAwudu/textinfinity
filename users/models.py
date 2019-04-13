from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from wallet.models import Wallet


class User(AbstractUser):
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return str(self.username + ' is added')
