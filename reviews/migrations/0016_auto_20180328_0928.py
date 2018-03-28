# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-03-28 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0015_remove_userprofile_website'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='UID',
        ),
        migrations.AddField(
            model_name='game',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='game',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
