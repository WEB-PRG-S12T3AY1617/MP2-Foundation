# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-22 01:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0003_auto_20170722_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_word',
            field=models.CharField(max_length=199),
        ),
    ]
