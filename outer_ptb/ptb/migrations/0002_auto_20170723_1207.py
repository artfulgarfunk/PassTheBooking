# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-23 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='bathrooms',
            field=models.PositiveIntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='bedrooms',
            field=models.PositiveIntegerField(default='2'),
            preserve_default=False,
        ),
    ]
