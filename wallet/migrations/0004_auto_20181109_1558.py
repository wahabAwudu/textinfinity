# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-11-09 21:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wallet', '0003_auto_20181109_0412'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deposit',
            name='ref_code',
            field=models.CharField(default='0GEHO8DX5I', editable=False, max_length=10, unique=True),
        ),
    ]
