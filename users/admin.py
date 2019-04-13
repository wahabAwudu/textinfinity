from django.contrib import admin

from .models import User


class UserModelAdmin(admin.ModelAdmin):
    model = User
    list_display = ['username', 'email', 'phone']


admin.site.register(User, UserModelAdmin)
