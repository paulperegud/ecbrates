# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-02 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecbrates', '0002_auto_20160201_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ecbrate',
            name='id',
        ),
        migrations.AddField(
            model_name='ecbrate',
            name='_key',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False, verbose_name='primary key, combination of date and code'),
            preserve_default=False,
        ),
    ]
