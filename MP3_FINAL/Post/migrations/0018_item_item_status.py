# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-12 03:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0017_remove_item_item_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_status',
            field=models.IntegerField(default=0),
        ),
    ]
