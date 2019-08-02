# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-01 17:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20190801_1158'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('forma_pago', models.CharField(max_length=30)),
                ('id_transaccion', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('fecha_pago', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('codigo_cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente')),
            ],
        ),
    ]
