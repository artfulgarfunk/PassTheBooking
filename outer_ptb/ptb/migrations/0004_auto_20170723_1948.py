# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-23 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptb', '0003_property_pet_friendly'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date_from',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date_until',
            field=models.DateField(),
        ),
    ]
