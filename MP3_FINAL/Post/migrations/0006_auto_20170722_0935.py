# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-22 01:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0005_auto_20170722_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_word',
            field=models.CharField(max_length=201),
        ),
    ]
