# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-03-23 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_auto_20180323_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game',
            field=models.CharField(max_length=100),
        ),
    ]
