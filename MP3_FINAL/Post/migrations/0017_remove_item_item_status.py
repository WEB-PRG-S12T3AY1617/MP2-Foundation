# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-12 03:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0016_auto_20170728_0221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item_status',
        ),
    ]
