# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-06 00:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_auto_20190803_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='password',
            field=models.CharField(default=True, max_length=30),
        ),
        migrations.AddField(
            model_name='cliente',
            name='usuario',
            field=models.CharField(default=True, max_length=30),
        ),
    ]