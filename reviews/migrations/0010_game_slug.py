# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-03-23 10:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_auto_20180323_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2018, 3, 23, 10, 54, 38, 983997, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
    ]
