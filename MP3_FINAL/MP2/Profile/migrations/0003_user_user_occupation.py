# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-21 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_auto_20170721_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_occupation',
            field=models.IntegerField(default=0),
        ),
    ]
