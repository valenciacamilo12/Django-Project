# Generated by Django 2.2.3 on 2019-08-02 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='gama',
        ),
    ]
