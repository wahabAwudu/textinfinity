from django.db import models
from django.conf import settings
import random
import string


class Wallet(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    current_balance = models.BigIntegerField(default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class Deposit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    ref_code = models.CharField(unique=True, editable=False, max_length=10)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    def get_ref_code(self):
        ref_code = settings.DEPOSIT_PREFIX + ''.join(random.sample((string.digits+string.ascii_uppercase), 7))
        new_ref_code = ref_code
        i = 0
        while Deposit.objects.filter(ref_code=new_ref_code).exists():
            new_ref_code = settings.DEPOSIT_PREFIX + ''.join(random.sample((string.digits+string.ascii_uppercase), 7))
            i = i+1
        return new_ref_code

    def save(self, *args, **kwargs):
        if not self.ref_code:
            self.ref_code = self.get_ref_code()
        return super().save(*args, **kwargs)
