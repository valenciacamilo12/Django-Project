# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-06 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20190805_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='codigo_cliente',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]