# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-11-12 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='status',
            field=models.CharField(default='ACTIVE', max_length=20),
        ),
    ]
