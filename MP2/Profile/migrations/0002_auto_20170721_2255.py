# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-21 14:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_degreefk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Profile.Degree'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_officefk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Profile.Office'),
        ),
    ]
