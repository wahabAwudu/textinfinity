# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-03-24 05:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_list_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('digits', models.CharField(max_length=15)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lists.List')),
            ],
        ),
    ]
