# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-06 16:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_auto_20190806_0853'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedidos',
            options={'permissions': set([('is_uno', 'Usuario Uno'), ('is_dos', 'Usuario Dos')])},
        ),
    ]
